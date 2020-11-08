from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django .shortcuts import redirect
from .models import ParkingUserModel
from .forms import ParkingForm
import datetime

# Create your views here.


def index(request):
    params = {
        'apikey': 'AIzaSyAmulNAl7XvDORhZ8f5HGJPm1uwJEHOqDg',
    }
    return render(request, 'parking_req/map1.html', params)

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
        return render(request, 'parking_req/create.html', self.params)


    def post(self, request):
        dt_now = datetime.datetime.now()
        user_id = request.session['user_id']
        coordinate = request.POST['coordinate']
        day = dt_now
        parking_type = request.POST['parking_type']
        width = request.POST['width']
        length = request.POST['length']
        height = request.POST['height']
        record = ParkingUserModel(user_id = user_id, coordinate = coordinate, day = day, \
            parking_type = parking_type, width = width, length = length, height = height)
        obj = ParkingUserModel()
        parking = ParkingForm(request.POST, instance=obj)
        self.params['form'] = parking
        if (parking.is_valid()):
            record.save()
            return redirect(to='/parking_req')
            
        return render(request, 'parking_req/create.html', self.params)

def edit(request, num):
    obj = ParkingUserModel.objects.get(id=num)
    params = {
        'title': 'ParkingEdit',
        'form': ParkingForm(instance=obj),
        'id':num,
    }
    if (request.method == 'POST'):    
        parking = ParkingForm(request.POST, instance=obj)
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
    params = {
        'title': 'ParkingDelete',
        'message': '※以下のレコードを削除します。',
        'id': num,
        'obj': parking,
    }
    return render(request, 'parking_req/delete.html', params)