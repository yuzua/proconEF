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

def test_ajax_response(request):
    input_text = request.POST.getlist("name_input_text")
    hoge = "Ajax Response: " + input_text[0]

    return HttpResponse(hoge)

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
    return render(request, "carsharing_booking/map.html", params)

def booking(request, num):
    params = {
        'parking_obj': '',
        'form': BookingCreateForm(),
        'message': '予約入力',
        'car_obj': '',
        'car_id': '',
    }

    parking_obj = ParkingUserModel.objects.get(id=num)
    params['parking_obj'] = parking_obj
    items = CarInfoParkingModel.objects.filter(parking_id=num).values('car_id')
    for item in items:
        index = item['car_id']
    params['car_id'] = index
    car_obj = CarInfoModel.objects.get(id=index)    
    params['car_obj'] = car_obj
    
    return render(request, 'carsharing_booking/booking.html', params)

def postBooking(request):
    if (request.method == 'POST'):
        user_id = request.session['user_id']
        car_id = request.POST['car_id']
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        record = BookingModel(user_id=user_id, car_id=car_id, start_day=start_day, start_time=start_time, end_day=end_day, end_time=end_time)
        record.save()
    messages.success(request, '予約が完了しました')
    return redirect(to='/carsharing_req/index')

class ReservationList(TemplateView):
    def __init__(self):
        self.params = {
            'title': '予約一覧',
            'data': ''
        }
    
    def get(self, request):
        booking = BookingModel.objects.filter(user_id=request.session['user_id']).order_by('-end_day', '-end_time')
        self.params['data'] = booking
        return render(request, 'carsharing_booking/list.html', self.params)
