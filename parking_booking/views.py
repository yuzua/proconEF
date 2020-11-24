from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django .shortcuts import redirect
from carsharing_req .models import CarsharUserModel
from owners_req .models import CarInfoParkingModel
from parking_req .models import *
import json
from .models import BookingInfoModel
from .forms import BookingInfoForm

# Create your views here.

def index(request):
    return HttpResponse('parking_booking')

def test(request):
    input_parking_id = request.POST.getlist("name_parking_id")
    request.session['user_parking_id'] = input_parking_id[0]
    return redirect(to='/parking_booking/create')    

# def test_ajax_app(request):
#     if str(request.user) == "AnonymousUser":
#         print('ゲスト')
#     else:
#         print(request.user)
#     hoge = "Hello Django!!"

#     return render(request, "carsharing_booking/index.html", {
#         "hoge": hoge,
#     })

# def test_ajax_response(request):
#     input_text = request.POST.getlist("name_input_text")
#     hoge = "Ajax Response: " + input_text[0]

#     return HttpResponse(hoge)

def map(request):
    data = CarsharUserModel.objects.get(id=request.session['user_id'])
    print(data.pref01+data.addr01+data.addr02)
    add = data.pref01+data.addr01+data.addr02
    set_list = CarInfoParkingModel.objects.values("parking_id")
    item_all = ParkingUserModel.objects.exclude(id__in=set_list)
    item = item_all.values("id", "user_id", "lat", "lng")
    item_list = list(item.all())
    print(item)
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
    return render(request, "parking_booking/map.html", params)

#駐車場予約
class ParkingBookingCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'ParkingBookingCreate',
            'message': 'Not found your data.<br>Please send your profile.',
            'form': BookingInfoForm(),
        }
    
    #ログインユーザ、非ログインユーザ判別
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            return redirect(to='/carsharing_req/index')
        else:
            print(request.user)
            #print(request.session['user_lat'])
            #print(request.session['user_lng'])

        return render(request, 'parking_booking/create.html', self.params)

    #入力データ保存
    def post(self, request):
        user_id = request.session['user_id']
        parking_id = request.session['user_parking_id']
        car_id = request.POST['car_id']
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        charge = request.POST['charge']
        record = BookingInfoModel(user_id = user_id, parking_id = parking_id, car_id=car_id, start_day = start_day, \
            end_day = end_day, start_time = start_time, end_time = end_time, charge = charge)
        obj = BookingInfoModel()
        p_b = BookingInfoForm(request.POST, instance=obj)
        self.params['form'] = p_b
        #バリデーションチェック
        if (p_b.is_valid()):
            record.save()
            return redirect(to='/parking_booking/')
            
        return render(request, 'parking_booking/create.html', self.params)

