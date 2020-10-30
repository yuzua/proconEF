from django.shortcuts import render
from django.http import HttpResponse
from django .shortcuts import redirect
from .models import ParkingUserModel
from .forms import ParkingForm
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the parking_req index.")

def create(request):
    if (request.method == 'POST'):
        obj = ParkingUserModel()
        parking = ParkingForm(request.POST, isinstance=obj)
        parking.save()
        return redirect(to='/parking_req')
    params = {
        'form': ParkingForm()
    }
    return render(request, 'parking_req/create.html', params)    