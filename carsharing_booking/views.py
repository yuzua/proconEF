from django.shortcuts import render
from django.http import HttpResponse
from carsharing_req .models import CarsharUserModel
from parking_req .models import *
from owners_req .models import CarInfoParkingModel, CarInfoModel
from carsharing_booking .models import BookingModel
from .forms import BookingCreateForm
import json
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
    parking_obj = ParkingUserModel.objects.get(id=num)
    items = CarInfoParkingModel.objects.filter(parking_id=num).values('car_id')
    for item in items:
        index = item['car_id']
    car_obj = CarInfoModel.objects.get(id=index)
    params = {
        'parking_obj': parking_obj,
        'form': BookingCreateForm(),
        'message': '予約入力',
        'car_obj': car_obj,
    }
    
    return render(request, 'carsharing_booking/booking.html', params)