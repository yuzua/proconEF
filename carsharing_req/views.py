from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
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
            ')</b><br>Your mail address is <b>' + request.POST['email'] + \
            '</b><br>Thank you send to me!'
        self.params['message'] = msg
        self.params['form'] = CarsharUserCreateForm(request.POST)
        return render(request, 'carsharing_req/index.html', self.params)

class CarsharUserSendMail(generic.FormView):

    template_name = "carsharing_req/index.html"
    form_class = CarsharUserCreateForm
    success_url = reverse_lazy('carsharing_req:index')


    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)