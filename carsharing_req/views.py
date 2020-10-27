from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import CarsharUserCreateForm
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the carsharing_req index.")


class CarsharUser(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'Not found your data.<br>Please send your profile.',
            'form': CarsharUserCreateForm(),
            'link': 'other',
        }
    
    def get(self, request):
        return render(request, 'carsharing_req/index.html', self.params)
    
    def post(self, request):
        msg = 'Your name is <b>' + request.POST['name'] + \
            '(' + request.POST['age'] + \
            ')</b><br>Your mail address is <b>' + request.POST['mail'] + \
            '</b><br>Thank you send to me!'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'carsharing_req/index.html', self.params)
