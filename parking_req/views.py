from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django .shortcuts import redirect
from .models import ParkingUserModel
from .forms import ParkingForm
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the parking_req index.")

class ParkingHostCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'ParkingHostCreate',
            'message': 'Not found your data.<br>Please send your profile.',
            'form': ParkingForm(),
        }
    
    def get(self, request):
        return render(request, 'parking_req/create.html', self.params)


    def post(self, request):
        obj = ParkingUserModel()
        parking = ParkingForm(request.POST, instance=obj)
        parking.save()
        return redirect(to='/parking_req')

    
