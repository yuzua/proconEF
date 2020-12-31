from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from carsharing_req .models import CarsharUserModel
from parking_req .models import ParkingUserModel
from owners_req .models import ParentCategory, Category, CarInfoParkingModel, CarInfoModel
from carsharing_booking .models import BookingModel
from parking_booking .models import ParkingBookingModel
from .forms import BookingCreateForm, CarCategory
import json, datetime
from django.contrib import messages
from django.db.models import Q
from django.core.mail import EmailMessage
# Create your views here.


def select(request):
    return render(request, "carsharing_booking/index.html", {
        "title": 'カーシェアリング予約',
    })

def test_ajax_app(request):
    if str(request.user) == "AnonymousUser":
        print('ゲスト')
    else:
        print(request.user)
    hoge = "Hello Django!!"

    return render(request, "carsharing_booking/ajax.html", {
        "hoge": hoge,
    })


def map(request):
    if request.user.id == None:
        add = '千葉県柏市末広町10-1'
    else:
        data = CarsharUserModel.objects.get(id=request.session['user_id'])
        print(data.pref01+data.addr01+data.addr02)
        add = data.pref01+data.addr01+data.addr02
    set_list = CarInfoParkingModel.objects.values("parking_id")
    item_all = ParkingUserModel.objects.filter(id__in=set_list)
    item = item_all.values("id", "address", "user_id", "lat", "lng")
    item_list = list(item.all())
    data = {
        'markerData': item_list,
    }
    params = {
        'name': '自宅',
        'add': add,
        'data_json': json.dumps(data)
    }
    if (request.method == 'POST'):
        params['add'] = request.POST['add']
        params['name'] = '検索'
    return render(request, "carsharing_booking/map.html", params)

def car(request):
    max_num = CarInfoModel.objects.values('category').order_by('parent_category', 'category').last()
    max_num = max_num.get('category') + 1
    set_QuerySet_car = CarInfoParkingModel.objects.values("car_id")
    set_QuerySet_parking = CarInfoParkingModel.objects.values("parking_id", "car_id")
    addadd = {}
    for index in set_QuerySet_parking:
        address = list(ParkingUserModel.objects.filter(id=index['parking_id']).values("address"))
        address = address[0]['address']
        index = index['car_id']
        addadd.setdefault(index, address)
    # print(addadd)

    item_all = CarInfoModel.objects.filter(id__in=set_QuerySet_car).order_by('parent_category', 'category')
    # print(item_all.values('category'))
    dict_car = {}
    for key in range(1, max_num):
        value = list(CarInfoModel.objects.select_related('parent_category__parent_category').select_related('category__category').filter(category=key).values('id', 'parent_category__parent_category', 'category__category', 'model_id', 'people', 'used_years'))
        if not value :
            print('空')
        else:
            for num in range(1, len(value)+1):
                if num == 1:
                    value[0]['address'] = addadd[value[0]['id']]
                    print(value[0])
                else:
                    print(num)
                    value[num-1]['address'] = addadd[value[num-1]['id']]
        dict_car.setdefault(key, value)
        # print(key, value)

    print(dict_car)
    params = {
        'car_obj': item_all,
        'form': CarCategory(),
        'parentcategory_list': list(ParentCategory.objects.all()),
        'category_set': list(Category.objects.all().values()),
        'json_car': json.dumps(dict_car, ensure_ascii=False)
    }
    return render(request, "carsharing_booking/car.html", params)

    print(dict_car)
    params = {
        'car_obj': item_all,
        'form': CarCategory(),
        'parentcategory_list': list(ParentCategory.objects.all()),
        'category_set': list(Category.objects.all().values()),
        'json_car': json.dumps(dict_car, ensure_ascii=False)
    }
    return render(request, "carsharing_booking/car.html", params)

def booking_car(request, num):
    request.session['select'] = "car"
    params = {
        'title': '予約',
        'events': '',
        'car_id': num,
        'form': BookingCreateForm(),
        'car_data': CarInfoModel.objects.get(id=num)
    }
    events = []
    # カーシェアリング予約
    booking = BookingModel.objects.filter(car_id=num).exclude(charge=-1).order_by('end_day', 'end_time')
    booking = booking.values("id", "start_day", "start_time", "end_day", "end_time")
    for obj in booking:
        title = obj.get("id")
        start = obj.get("start_day") + 'T' + obj.get("start_time")
        end = obj.get("end_day") + 'T' + obj.get("end_time")
        event = dict((['title', 'カーシェアリング予約'+str(title)], ['start', start], ['end', end], ['color', '#A9A9A9']))
        events.append(event)
    # 車両貸し出し制限
    loaning = BookingModel.objects.filter(car_id=num, charge=-1).order_by('end_day', 'end_time')
    loaning = loaning.values("id", "start_day", "start_time", "end_day", "end_time")
    for obj in loaning:
        title = obj.get("id")
        start = obj.get("start_day") + 'T' + obj.get("start_time")
        end = obj.get("end_day") + 'T' + obj.get("end_time")
        event = dict((['title', '車両貸し出し'+str(title)], ['start', start], ['end', end], ['color', '#DC143C']))
        events.append(event)

    request.session['events'] = json.dumps(events)
    params['events'] = request.session['events']
    car_obj = CarInfoModel.objects.filter(id=num)
    request.session['car_objs'] = car_obj
    # parking_id = CarInfoParkingModel.objects.filter(car_id=num).values('parking_id')
    # request.session['parking_id'] = parking_id[0]['parking_id']
    request.session['obj_id'] = num

    return render(request, "carsharing_booking/car_next.html", params)


def booking(request, num):
    request.session['select'] = "map"
    request.session['obj_id'] = num
    params = {
        'form': BookingCreateForm(),
        'message': '予約入力',
        'car_objs': '',
        'car_id': '',
        'num': request.session['obj_id'],
    }
    num = request.session['obj_id']
    address = ParkingUserModel.objects.filter(id=request.session['obj_id']).values('address')
    params['address'] = address[0]['address']
    items = CarInfoParkingModel.objects.filter(parking_id=num).values('car_id')
    print(items)
    car_list = []
    for item in items:
        index = item['car_id']
    # params['car_id'] = index
        car_list.append(index)
        car_obj = CarInfoModel.objects.filter(id__in=car_list)
    params['car_objs'] = car_obj
    request.session['car_objs'] = car_obj

    event_dict = {}
    # カーシェアリング予約
    for carnum in car_list:
        events = []
        booking = BookingModel.objects.filter(car_id=carnum).exclude(charge=-1).order_by('end_day', 'end_time')
        booking = booking.values("id", "start_day", "start_time", "end_day", "end_time")
        for obj in booking:
            title = obj.get("id")
            start = obj.get("start_day") + 'T' + obj.get("start_time")
            end = obj.get("end_day") + 'T' + obj.get("end_time")
            event = dict((['title', 'カーシェアリング予約'+str(title)], ['start', start], ['end', end], ['color', '#A9A9A9']))
            events.append(event)
        # 車両貸し出し制限
        loaning = BookingModel.objects.filter(car_id=carnum, charge=-1).order_by('end_day', 'end_time')
        loaning = loaning.values("id", "start_day", "start_time", "end_day", "end_time")
        for obj in loaning:
            title = obj.get("id")
            start = obj.get("start_day") + 'T' + obj.get("start_time")
            end = obj.get("end_day") + 'T' + obj.get("end_time")
            event = dict((['title', '車両貸し出し'+str(title)], ['start', start], ['end', end], ['color', '#DC143C']))
            events.append(event)
        event_dict[carnum] = events
    request.session['events'] = json.dumps(event_dict)
    params['events'] = request.session['events']
    print(event_dict)

    
    return render(request, 'carsharing_booking/booking.html', params)

def checkBooking(request):
    params = {
        'parking_obj': '',
        'title': 'カーシェアリング予約確認',
        'message': '予約情報確認',
        'data': '',
        'kingaku': '',
        'times': '',
        'car_obj': '',
        'car_objs': request.session['car_objs'],
        'address': '',

    }
    # error時の入力保存しredirect
    if request.session['select'] == 'map':
        address = ParkingUserModel.objects.filter(id=request.session['obj_id']).values('address')
        params['address'] = address[0]['address']
    elif request.session['select'] == 'car':
        params['car_id'] = request.session['obj_id']
    params['events'] = request.session['events']
    obj = BookingModel()
    c_b = BookingCreateForm(request.POST, instance=obj)
    params['form'] = c_b
        
    

    # POSTデータを変数へ格納
    start_day = request.POST['start_day']
    end_day = request.POST['end_day']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']

    # POSTデータをdatetime型へ変換
    start = start_day + ' ' + start_time
    start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M')
    print(start)
    print(type(start))
    end = end_day + ' ' + end_time
    end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M')
    print(end)
    print(type(end))

    booking_list = BookingModel.objects.filter(car_id=request.POST['car_id'])
    booking_list = booking_list.filter(Q(start_day=start_day) | Q(start_day=end_day) | Q(end_day=start_day) | Q(end_day=end_day))
    # print(booking_list)
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
            messages.error(request, '申し訳ございません。その時間帯は既に予約済みです。別の車両にするか時間帯を変更してください。<br>' + datetime.datetime.strftime(booking_start, "%Y年%m月%d日 %H:%M") + ' 〜 ' + datetime.datetime.strftime(booking_end, "%Y年%m月%d日 %H:%M"))
            if request.session['select'] == 'map':
                return render(request, 'carsharing_booking/booking.html', params)
            elif request.session['select'] == 'car':
                return render(request, "carsharing_booking/car_next.html", params)
        else:
            print("大丈夫！")

    print(booking_list)

    # charge = request.POST['charge']
    
    time = end - start
    d = int(time.days)
    m = int(time.seconds / 60)
    print(d)
    print(int(m))
    charge = 0
    times = ''

    if d <= 0:
        print('1day')
    else:
        print('days')
        charge = int(d * 10000)
        times = str(d) + '日 '

    if start_time < end_time:
        print('tule')
        charge += int(m / 15 * 330)
        h = int(m / 60)
        m = int(m % 60)
        x = str(h) + '時間 ' + str(m) + '分'
        times += x
    elif start_time >= end_time and d < 0:
        print('false')
        messages.error(request, '終了時刻が開始時刻よりも前です。')
        if request.session['select'] == 'map':
            return render(request, 'carsharing_booking/booking.html', params)
        elif request.session['select'] == 'car':
            return render(request, "carsharing_booking/car_next.html", params)
    else:
        charge += int(m / 15 * 330)
        h = int(m / 60)
        m = int(m % 60)
        x = str(h) + '時間 ' + str(m) + '分'
        times += x
    if d == 0 and m < 15 and h == 0:
        messages.error(request, '15分以下は利用できません。')
        if request.session['select'] == 'map':
            return render(request, 'carsharing_booking/booking.html', params)
        elif request.session['select'] == 'car':
            return render(request, "carsharing_booking/car_next.html", params)
        
    data = {
        'car_id': request.POST['car_id'],
        'start_day': start_day,
        'start_time': start_time,
        'end_day': end_day,
        'end_time': end_time,
        'charge': charge,
    }
    if request.session['select'] == 'map':
        address = ParkingUserModel.objects.filter(id=request.session['obj_id']).values('address')
    elif request.session['select'] == 'car':
        parking_id = CarInfoParkingModel.objects.filter(car_id=request.session['obj_id']).values('parking_id')
        print(parking_id)
        address = ParkingUserModel.objects.filter(id=parking_id[0]['parking_id']).values('address')
        print(address)
    params['address'] = address[0]['address']
    params['kingaku'] = "{:,}".format(charge)
    params['data'] = data
    params['times'] = times
    params['car_obj'] = CarInfoModel.objects.get(id=request.POST['car_id'])
    messages.warning(request, 'まだ予約完了しておりません。<br>こちらの内容で宜しければ確定ボタンをクリックして下さい。')
    return render(request, "carsharing_booking/check.html", params)

def push(request):
    if (request.method == 'POST'):
        user_id = int(request.session['user_id'])
        car_id = int(request.POST['car_id'])
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        charge = int(request.POST['charge'])
        record = BookingModel(user_id=user_id, car_id=car_id, start_day=start_day, start_time=start_time, end_day=end_day, end_time=end_time, charge=charge)
        record.save()
        del request.session['events']
        del request.session['car_objs']
        del request.session['obj_id']
        del request.session['select']
        messages.success(request, '予約が完了しました。<br>ご登録されているメールアドレスに予約完了メールを送信致しました。ご確認下さい。')
        #mail送信メソッドの呼び出し
        success_booking_mail(request, charge, start_day, start_time, end_day, end_time)
    else:
        messages.error(request, '不正なリクエストです')
    return redirect(to='/carsharing_booking/reservation')


def success_booking_mail(request, charge, start_day, start_time, end_day, end_time):

    subject = "予約完了確認メール"
    url = 'http://127.0.0.1:8000/carsharing_booking/list/'
    message = str(request.user) + "様\n \
        ご予約ありがとうございます。\n \
        お手続きが完了いたしました。\n\n \
        開始日:" + start_day + "\n \
        開始時刻:" + start_time + "\n \
        終了日:" + end_day + "\n \
        終了時刻:" + end_time + "\n \
        料金:" + str(charge) + "円\n\n \
        予約詳細はコチラから！！\n \
        URL: " + url + "\n"
    user = request.user  # ログインユーザーを取得する
    from_email = 'admin@gmail.com'  # 送信者
    user.email_user(subject, message, from_email)  # メールの送信
    pass

def reservation(request):
    booking = BookingModel.objects.filter(user_id=request.session['user_id']).values('id', 'car_id', 'start_day', 'start_time', 'end_day', 'end_time', 'charge').last()
    data = {
        'car_id': booking['car_id'],
        'start_day': booking['start_day'],
        'start_time': booking['start_time'],
        'end_day': booking['end_day'],
        'end_time': booking['end_time'],
        'charge': booking['charge'],
    }
    car_obj = CarInfoModel.objects.get(id=booking['car_id'])
    parking_id = CarInfoParkingModel.objects.filter(car_id=booking['car_id']).values('parking_id')
    address = ParkingUserModel.objects.filter(id=parking_id[0]['parking_id']).values('address')
    add = address[0]['address']

    # str型をdatetime型へ変換
    start = booking['start_day'] + ' ' + booking['start_time']
    start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M')
    end = booking['end_day'] + ' ' + booking['end_time']
    end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M')

    # 日にち　分数計算
    time = end - start
    d = int(time.days)
    m = int(time.seconds / 60)
    times = ''

    # 利用合計日時計算
    if d <= 0:
        print('1day')
    else:
        times = str(d) + '日 '

    if booking['start_time'] < booking['end_time']:
        h = int(m / 60)
        m = int(m % 60)
        x = str(h) + '時間 ' + str(m) + '分'
        times += x
    else:
        charge += int(m / 15 * 330)
        h = int(m / 60)
        m = int(m % 60)
        x = str(h) + '時間 ' + str(m) + '分'
        times += x

    params = {
        'title': '予約完了',
        'message': '予約情報',
        'address': add,
        'car_obj': car_obj,
        'data': data,
        'times': times,
        'kingaku': '',
    }
    params['kingaku'] = "{:,}".format(booking['charge'])
    return render(request, "carsharing_booking/check.html", params)


#予約確認・一覧
class ReservationList(TemplateView):
    def __init__(self):
        self.params = {
            'title': '予約一覧',
            'data': '',
            'data2': '',
        }
    
    def get(self, request):
        dt_now = datetime.datetime.now()
        d_now = dt_now.strftime('%Y-%m-%d')
        print(d_now)
        booking = BookingModel.objects.filter(user_id=request.session['user_id'], end_day__gt=dt_now).exclude(charge=-1).order_by('-end_day', '-end_time').values('id', 'user_id', 'car_id', 'start_day', 'start_time', 'end_day', 'end_time', 'charge')
        self.params['data'] = booking
        booking2 = ParkingBookingModel.objects.filter(user_id=request.session['user_id'], end_day__gt=dt_now).exclude(charge=-1).order_by('-end_day', '-end_time').values('id', 'user_id', 'parking_id', 'start_day', 'start_time', 'end_day', 'end_time', 'charge')
        self.params['data'] = booking
        self.params['data2'] = booking2

        for item in list(booking):
            print(item['car_id'])
            num = CarInfoModel.objects.filter(id=item['car_id']).values("category")
            category = Category.objects.filter(id=num[0]['category']).values("category")
            item['category'] = category[0]['category']
            parking_id = CarInfoParkingModel.objects.filter(car_id=item['car_id']).values("parking_id")
            address = ParkingUserModel.objects.filter(id=parking_id[0]['parking_id']).values("address")
            item['address'] = address[0]['address']
            print(item)
        for item in list(booking2):
            address = ParkingUserModel.objects.filter(id=item['parking_id']).values("address")
            item['address'] = address[0]['address']
            print(item)
        return render(request, 'carsharing_booking/list.html', self.params)
