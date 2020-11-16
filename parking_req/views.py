from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django .shortcuts import redirect
from carsharing_req .models import CarsharUserModel
from .models import ParkingUserModel
from .forms import ParkingForm
import datetime
import json

# Create your views here.


def index(request):
    params = {
        'hoge': '',
    }
    return render(request, 'parking_req/map1.html', params)


def test_ajax_response(request):
    input_lat = request.POST.getlist("name_input_lat")
    input_lng = request.POST.getlist("name_input_lng")
    hoge = "lat: "  + input_lat[0] + "lng: " + input_lng[0] + "がセットされました"
    request.session['user_lat'] = input_lat[0]
    request.session['user_lng'] = input_lng[0]

    return HttpResponse(hoge)

class ParkingHostCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'ParkingHostCreate',
            'message': 'Not found your data.<br>Please send your profile.',
            'form': ParkingForm(),
        }
    
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            return redirect(to='/carsharing_req/index')
        else:
            print(request.user)
            print(request.session['user_lat'])
            print(request.session['user_lng'])

        return render(request, 'parking_req/create.html', self.params)


    def post(self, request):
        dt_now = datetime.datetime.now()
        user_id = request.session['user_id']
        lat = request.session['user_lat']
        lng = request.session['user_lng']
        day = dt_now
        parking_type = request.POST['parking_type']
        width = request.POST['width']
        length = request.POST['length']
        height = request.POST['height']
        record = ParkingUserModel(user_id = user_id, lat = lat, lng=lng, day = day, \
            parking_type = parking_type, width = width, length = length, height = height)
        obj = ParkingUserModel()
        parking = ParkingForm(request.POST, instance=obj)
        self.params['form'] = parking
        if (parking.is_valid()):
            record.save()
            del request.session['user_lat']
            del request.session['user_lng']
            return redirect(to='/parking_req')
            
        return render(request, 'parking_req/create.html', self.params)

def edit(request):
    # num = request.POST['message']
    # obj = ParkingUserModel.objects.filter(id=num).all()
    # params = {
    #     'title': 'ParkingEdit',
    #     'data': obj,
    #     'message':num,
    #     'form': ParkingForm(instance=obj),
    # }
    # return render(request, 'parking_req/edit.html', params)
    if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = ParkingUserModel.objects.get(id=num)
        parking = ParkingForm(request.POST, instance=obj)
        params = {
            'title':'ParkingEdittest', 
            'form': ParkingForm(),
            'id':num,
        }
        if (parking.is_valid()):
            parking.save()
            return redirect(to='/parking_req')
        else:
            params['form'] = ParkingForm(request.POST, instance= obj)        
        
    return render(request, 'parking_req/edit.html', params)

def delete(request, num):
    parking = ParkingUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        parking.delete()
        return redirect(to='/parking_req')
    # params = {
    #     'title': 'ParkingDelete',
    #     'message': '※以下のレコードを削除します。',
    #     'obj': parking,
    #     'id': num,
    # }
    return render(request, 'parking_req/delete.html')

def sample(request):
    s_p = ParkingUserModel.objects.filter(user_id=request.session['user_id'])
    sample_parking = s_p.values("id", "user_id", "lat", "lng")
    if (request.method == 'POST'):
        num = request.POST['obj.id']
        num1 = request.POST['command']
        #edit
        if (num1 == 'edit'):
            obj = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingEdit',
            'id':num,
            'form': ParkingForm(instance=obj), 
            }
            return render(request, 'parking_req/edit.html', params)
        #delete    
        if (num1 == 'delete'):
            delete_parking = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingDelete',
            'message': '※以下のレコードを削除します。',
            'obj': delete_parking,
            'id': num,
            }
            return render(request, 'parking_req/delete.html', params)
    else:
        data = CarsharUserModel.objects.get(id=request.session['user_id'])
        print(data.pref01+data.addr01+data.addr02)
        add = data.pref01+data.addr01+data.addr02
        #sample
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
        return render(request, 'parking_req/map3.html', params)