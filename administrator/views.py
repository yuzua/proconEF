from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django .shortcuts import redirect
from parking_req .models import ParkingUserModel
from parking_req .forms import ParkingForm
import datetime

# Create your views here.
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
            return redirect(to='/administrator')
            
        return render(request, 'administrator/create.html', self.params)    
