from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django .shortcuts import redirect
from carsharing_req .models import CarsharUserModel
from .models import ParkingUserModel
from .forms import ParkingForm, ParkingLoaningForm
from parking_booking .models import ParkingBookingModel
import datetime
import json
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def index(request):
    params = {
        'msg': '',
    }
    return render(request, 'parking_req/mapping.html', params)

#登録する緯度、経度をセッションにセット
def test_ajax_response(request):
    input_lat = request.POST.getlist("name_input_lat")
    input_lng = request.POST.getlist("name_input_lng")
    hoge = "lat: "  + input_lat[0] + "lng: " + input_lng[0] + "がセットされました"
    request.session['user_lat'] = input_lat[0]
    request.session['user_lng'] = input_lng[0]

    return HttpResponse(hoge)

#駐車場データ登録機能
class ParkingHostCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'ParkingHostCreate',
            'message': '駐車場情報入力',
            'form': ParkingForm(),
        }
    
    #ログインユーザ、非ログインユーザ判別
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index')
        else:
            print(request.user)
            print(request.session['user_lat'])
            print(request.session['user_lng'])
            self.params['lat'] = request.session['user_lat']
            self.params['lng'] = request.session['user_lng']

        return render(request, 'parking_req/create.html', self.params)

    #入力データとセッションデータを保存
    def post(self, request):
        dt_now = datetime.datetime.now()
        user_id = request.session['user_id']
        address = request.POST['address']
        lat = request.session['user_lat']
        lng = request.session['user_lng']
        day = dt_now
        parking_type = request.POST['parking_type']
        width = request.POST['width']
        length = request.POST['length']
        height = request.POST['height']
        record = ParkingUserModel(user_id = user_id, address = address, lat = lat, lng=lng, day = day, \
            parking_type = parking_type, width = width, length = length, height = height)
        obj = ParkingUserModel()
        parking = ParkingForm(request.POST, instance=obj)
        self.params['form'] = parking
        #バリデーションチェック
        if (parking.is_valid()):
            record.save()
            #セッションデータ削除
            del request.session['user_lat']
            del request.session['user_lng']
            if 'info_flag' in request.session:
                print(request.session['info_flag'])
                return redirect(to='/owners_req/settinginfo')
            else:
                print('none')
                messages.success(self.request, '駐車場登録が完了しました。')
                return redirect(to='/parking_req/sample')
        return render(request, 'parking_req/create.html', self.params)

def edit(request):
    if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = ParkingUserModel.objects.get(id=num)
        parking = ParkingForm(request.POST, instance=obj)
        params = {
            'title':'ParkingEdit',
            'message': '駐車場情報修正', 
            'form': ParkingForm(),
            'id':num,
        }
        if (parking.is_valid()):
            parking.save()
            messages.success(request, '駐車場情報を修正しました。')
            return redirect(to='/parking_req/sample')
        else:
            params['form'] = ParkingForm(request.POST, instance= obj)        
        
    return render(request, 'parking_req/edit.html', params)

def delete(request, num):
    parking = ParkingUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        parking.delete()
        messages.success(request, '駐車場情報を削除しました。')
        return redirect(to='/parking_req/sample')

    return render(request, 'parking_req/delete.html')

def sample(request):
    s_p = ParkingUserModel.objects.filter(user_id=request.session['user_id'])
    sample_parking = s_p.values("id", "user_id", "lat", "lng", "address")
    if (request.method == 'POST'):
        num1 = request.POST['command']
        #修正機能
        if (num1 == 'edit'):
            num = request.POST['obj.id']
            obj = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingEdit',
            'message': '駐車場情報修正',
            'id':num,
            'form': ParkingForm(instance=obj), 
            }
            return render(request, 'parking_req/edit.html', params)
        #削除機能    
        if (num1 == 'delete'):
            num = request.POST['obj.id']
            delete_parking = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingDelete',
            'message': '駐車場情報削除',
            'obj': delete_parking,
            'id': num,
            }
            return render(request, 'parking_req/delete.html', params)
        #検索機能
        if (num1 == 'map'):
            data = CarsharUserModel.objects.get(id=request.session['user_id'])
            print(data.pref01+data.addr01+data.addr02)
            add = data.pref01+data.addr01+data.addr02
            markerData = list(sample_parking.all())
            #item_all = ParkingUserModel.objects.all()
            #item = item_all.values("id", "user_id", "lat", "lng")
            #item_list = list(item.all())
            #print(item)
            data = {
                'markerData': markerData,
            }
            params = {
            'name': '自宅',
            'add': add,
            'data_json': json.dumps(data)
            }
            if (request.method == 'POST'):
                params['add'] = request.POST['add']
            return render(request, "parking_req/parking_map.html", params)        
    else:
        #地図上に登録した駐車場を表示
        data = CarsharUserModel.objects.get(id=request.session['user_id'])
        print(data.pref01+data.addr01+data.addr02)
        add = data.pref01+data.addr01+data.addr02
        markerData = list(sample_parking.all())
        data = {
            'markerData': markerData,
        }
        params = {
            'title': 'ParkingSample',
            'message': '駐車場登録データ',
            'data': sample_parking,
            'name': '自宅',
            'add': add,
            'data_json': json.dumps(data)
        }
        # return render(request, 'parking_req/sample.html', params)
        return render(request, 'parking_req/parking_map.html', params)


class ParkingLoaningCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': '駐車場貸し出し日時登録',
            'message': '貸し出し不可日時入力',
            'form': ParkingLoaningForm(),
            'parking_obj': '',
        }
    
    #ログインユーザ、非ログインユーザ判別
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index')
        else:
            print(request.user)
            parking_obj = ParkingUserModel.objects.filter(user_id=request.session['user_id'], countflag=True)
            self.params['parking_obj'] = parking_obj
            print(parking_obj)

        return render(request, 'parking_req/loaning.html', self.params)

    #入力データ保存
    def post(self, request):
        # POSTデータを変数へ格納
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        request.session['user_parking_id'] = request.POST['parking_id']

        # POSTデータをdatetime型へ変換
        start = start_day + ' ' + start_time
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M')
        print(start)
        print(type(start))
        end = end_day + ' ' + end_time
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M')
        print(end)
        print(type(end))

        booking_list = ParkingBookingModel.objects.filter(parking_id=request.session['user_parking_id'])
        booking_list = booking_list.filter(Q(start_day=start_day) | Q(start_day=end_day) | Q(end_day=start_day) | Q(end_day=end_day))
        print(booking_list)
        booking_list = booking_list.values('id', 'start_day', 'start_time', 'end_day', 'end_time')
        for item in booking_list:
            booking_id = item['id']
            booking_sd = item['start_day']
            booking_st = item['start_time']
            booking_ed = item['end_day']
            booking_et = item['end_time']
            print('item')
            print(item)
            booking_start = booking_sd + ' ' + booking_st
            booking_start = datetime.datetime.strptime(booking_start, '%Y-%m-%d %H:%M')
            booking_end = booking_ed + ' ' + booking_et
            booking_end = datetime.datetime.strptime(booking_end, '%Y-%m-%d %H:%M')
            if start <= booking_end and end >= booking_start:
                print("被り！！")
                messages.error(request, '申し訳ございません。その時間帯は既に予約済みです。別の駐車場にするか時間帯を変更してください。<br>' \
                     + datetime.datetime.strftime(booking_start, "%Y年%m月%d日 %H:%M") + ' 〜 ' \
                     + datetime.datetime.strftime(booking_end, "%Y年%m月%d日 %H:%M"))
                return render(request, 'parking_req/loaning.html', self.params)
            else:
                print("大丈夫！")

        print(booking_list)

        time = end - start
        d = int(time.days)
        m = int(time.seconds / 60)
        print(d)
        print(int(m))
        times = ''

        if d <= 0:
            print('1day')
        else:
            print('days')
            times = str(d) + '日 '

        if start_time < end_time:
            print('tule')
            h = int(m / 60)
            m = int(m % 60)
            x = str(h) + '時間 ' + str(m) + '分'
            times += x
        elif start_time >= end_time and d < 0:
            print('false')
            obj = ParkingBookingModel()
            p_b = ParkingLoaningForm(request.POST, instance=obj)
            self.params['form'] = p_b
            messages.error(request, '終了時刻が開始時刻よりも前です。')
            parking_obj = ParkingUserModel.objects.filter(user_id=request.session['user_id'], countflag=True)
            self.params['parking_obj'] = parking_obj
            return render(request, 'parking_req/loaning.html', self.params)
        else:
            h = int(m / 60)
            m = int(m % 60)
            x = str(h) + '時間 ' + str(m) + '分'
            times += x
        
        charge = -1
        data = {
            'start_day': start_day,
            'start_time': start_time,
            'end_day': end_day,
            'end_time': end_time,
            'charge': charge,
        }
        self.params['kingaku'] = charge
        self.params['data'] = data
        self.params['times'] = times
        self.params['message'] += '情報確認'
        messages.warning(self.request, 'まだ貸し出し不可日時登録を完了しておりません。<br>こちらの内容で宜しければ確定ボタンをクリックして下さい。')
        return render(request, "parking_req/check.html", self.params)

def push(request):
    user_id = int(request.session['user_id'])
    parking_id = int(request.session['user_parking_id'])
    start_day = request.POST['start_day']
    end_day = request.POST['end_day']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    charge = int(request.POST['charge'])
    record = ParkingBookingModel(user_id = user_id, parking_id = parking_id, start_day = start_day, \
        end_day = end_day, start_time = start_time, end_time = end_time, charge = charge)
    record.save()
    messages.success(request, '登録が完了しました。')
    del request.session['user_parking_id']
    return redirect(to='parking_req:loaning')