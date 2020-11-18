from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django .shortcuts import redirect
from parking_req .models import ParkingUserModel
from carsharing_req .models import CarsharUserModel
from parking_req .forms import ParkingForm
import datetime
import json
from accounts .models import CustomUser

# Create your views here.
def check_superuser(request):
    if request.user.id == None:
        return redirect(to='/carsharing_req/index')
    flag = CustomUser.objects.filter(id=request.user.id)
    flag = flag.values('is_superuser')
    flag = flag[0]['is_superuser']
    if flag == True:
        print(request.user)
        return redirect(to='/administrator/index')
    else:
        return redirect(to='/carsharing_req/')

def index(request):
    params = {
        'hoge': '',
    }
    return render(request, 'administrator/index.html', params)


def test_ajax_response(request):
    input_lat = request.POST.getlist("name_input_lat")
    input_lng = request.POST.getlist("name_input_lng")
    hoge = "lat: "  + input_lat[0] + "lng: " + input_lng[0] + "がセットされました"
    request.session['user_lat'] = input_lat[0]
    request.session['user_lng'] = input_lng[0]

    return HttpResponse(hoge)

class ParkingAdminCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'ParkingAdminCreate',
            'message': 'Not found your data.<br>Please send your profile.',
            'form': ParkingForm(),
        }
    
    def get(self, request):
        return render(request, 'administrator/create.html', self.params)


    def post(self, request):
        dt_now = datetime.datetime.now()
        user_id = 0
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
            return redirect(to='/administrator/admin_main')
            
        return render(request, 'administrator/create.html', self.params)

def admin_main(request):
    s_p = ParkingUserModel.objects.filter(user_id=0)
    admin_parking = s_p.values("id", "user_id", "lat", "lng")
    if (request.method == 'POST'):
        num = request.POST['obj.id']
        num1 = request.POST['command']
        #edit
        if (num1 == 'edit'):
            obj = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingAdminEdit',
            'id':num,
            'form': ParkingForm(instance=obj), 
            }
            return render(request, 'administrator/edit.html', params)
        #delete    
        if (num1 == 'delete'):
            delete_parking = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingAdminDelete',
            'message': '※以下のレコードを削除します。',
            'obj': delete_parking,
            'id': num,
            }
            return render(request, 'administrator/delete.html', params)
    else:
        # data = CarsharUserModel.objects.get(id=0)
        # print(data.pref01+data.addr01+data.addr02)
        add = '千葉県柏市末広町10-1'
        #admin_main
        markerData = list(admin_parking.all())
        data = {
            'markerData': markerData,
        }
        params = {
            'title': 'ParkingAdminMain',
            'message': '駐車場登録データ',
            'data': admin_parking,
            'name': '自宅',
            'add': add,
            'data_json': json.dumps(data)
        }
        return render(request, 'administrator/admin_main.html', params)        

def edit(request):
    if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = ParkingUserModel.objects.get(id=num)
        parking = ParkingForm(request.POST, instance=obj)
        params = {
            'title':'ParkingAdminEdit', 
            'form': ParkingForm(),
            'id':num,
        }
        if (parking.is_valid()):
            parking.save()
            return redirect(to='/administrator/admin_main')
        else:
            params['form'] = ParkingForm(request.POST, instance= obj)        
        
    return render(request, 'administrator/edit.html', params)

def delete(request, num):
    parking = ParkingUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        parking.delete()
        return redirect(to='/administrator/admin_main')

    return render(request, 'administrator/delete.html')                
