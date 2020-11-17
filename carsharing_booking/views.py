from django.shortcuts import render
from django.http import HttpResponse
from carsharing_req .models import CarsharUserModel
from parking_req .models import *
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
    item_all = ParkingUserModel.objects.all()
    item = item_all.values("id", "user_id", "lat", "lng")
    item_list = list(item.all())
    print(item)
    data = {
        'markerData': item_list,
        # 'markerData': [
        #     {
        #         'name': 'TAM 東京',
        #         'lat': 35.6954806,
        #         'lng': 139.76325010000005,
        #         'icon': 'tam.png',
        #     }, {
        #         'name': '小川町駅',
        #         'lat': 35.6951212,
        #         'lng': 139.76610649999998
        #     }, {
        #         'name': '淡路町駅',
        #         'lat': 35.69496,
        #         'lng': 139.76746000000003
        #     }, {
        #         'name': '御茶ノ水駅',
        #         'lat': 35.6993529,
        #         'lng': 139.76526949999993
        #     }, {
        #         'name': '神保町駅',
        #         'lat': 35.695932,
        #         'lng': 139.75762699999996
        #     }, {
        #         'name': '新御茶ノ水駅',
        #         'lat': 35.696932,
        #         'lng': 139.76543200000003
        #     }
        # ],
    }
    params = {
        'name': '自宅',
        'add': add,
        'data_json': json.dumps(data)
    }
    if (request.method == 'POST'):
        params['add'] = request.POST['add']
    return render(request, "carsharing_booking/map.html", params)