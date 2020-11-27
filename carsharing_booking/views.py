from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from carsharing_req .models import CarsharUserModel
from parking_req .models import *
from owners_req .models import CarInfoParkingModel, CarInfoModel
from carsharing_booking .models import BookingModel
from .forms import BookingCreateForm
import json, datetime
from django.contrib import messages
# Create your views here.


def test_ajax_app(request):
    if str(request.user) == "AnonymousUser":
        print('ゲスト')
    else:
        print(request.user)
    hoge = "Hello Django!!"

    return render(request, "carsharing_booking/index.html", {
        "hoge": hoge,
    })


def map(request):
    data = CarsharUserModel.objects.get(id=request.session['user_id'])
    print(data.pref01+data.addr01+data.addr02)
    add = data.pref01+data.addr01+data.addr02
    set_list = CarInfoParkingModel.objects.values("parking_id")
    item_all = ParkingUserModel.objects.filter(id__in=set_list)
    item = item_all.values("id", "user_id", "lat", "lng")
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

def booking(request, num):
    params = {
        'parking_obj': '',
        'form': BookingCreateForm(),
        'message': '予約入力',
        'car_obj': '',
        'car_id': '',
        'num': num,
    }

    parking_obj = ParkingUserModel.objects.get(id=num)
    params['parking_obj'] = parking_obj
    items = CarInfoParkingModel.objects.filter(parking_id=num).values('car_id')
    for item in items:
        index = item['car_id']
    params['car_id'] = index
    car_obj = CarInfoModel.objects.get(id=index)    
    params['car_obj'] = car_obj
    request.session['car_obj'] = car_obj
    
    return render(request, 'carsharing_booking/booking.html', params)

def checkBooking(request):
    params = {
        'parking_obj': '',
        'title': 'カーシェアリング予約確認',
        'message': '予約情報確認',
        'data': '',
        'kingaku': '',
        'times': '',
        'car_obj': request.session['car_obj'],
        'address': request.POST['address'],
    }
    start_day = request.POST['start_day']
    end_day = request.POST['end_day']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    # charge = request.POST['charge']
    start = start_day + ' ' + start_time
    start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M')
    print(start)
    print(type(start))
    end = end_day + ' ' + end_time
    end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M')
    print(end)
    print(type(end))
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
        parking_obj = ParkingUserModel.objects.get(id=request.POST['num'])
        params['parking_obj'] = parking_obj
        obj = BookingModel()
        c_b = BookingCreateForm(request.POST, instance=obj)
        params['form'] = c_b
        messages.error(request, '終了時刻が開始時刻よりも前です。')
        return render(request, 'carsharing_booking/booking.html', params)
    else:
        charge += int(m / 15 * 330)
        h = int(m / 60)
        m = int(m % 60)
        x = str(h) + '時間 ' + str(m) + '分'
        times += x
        
    data = {
        'car_id': request.POST['car_id'],
        'start_day': start_day,
        'start_time': start_time,
        'end_day': end_day,
        'end_time': end_time,
        'charge': charge,
    }
    params['kingaku'] = "{:,}".format(charge)
    params['data'] = data
    params['times'] = times
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
    messages.success(request, '予約が完了しました')
    return redirect(to='/carsharing_req/index')

class ReservationList(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'カーシェアリング予約一覧',
            'data': ''
        }
    
    def get(self, request):
        booking = BookingModel.objects.filter(user_id=request.session['user_id']).order_by('-end_day', '-end_time')
        self.params['data'] = booking
        return render(request, 'carsharing_booking/list.html', self.params)
