from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HostUserModel, CarInfoModel
from .forms import HostUserForm, CarInfoForm
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the owners_req index.")

class CreateView(TemplateView):
    def __init__(self):
        self.params = {
        'title': 'カーシェアリングオーナー申請',
        'form': HostUserForm(),
    }
    def get(self, request):
        return render(request, 'owners_req/create.html', self.params)
    def post(self, request):
        obj = HostUserModel()
        owners = HostUserForm(request.POST, instance=obj)
        owners.save()
        return redirect(to='/owners_req')
    
def edit(request, num):
    obj = HostUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        owners2 = HostUserForm(request.POST, instance=obj)
        owners2.save()
        return redirect(to='/owners_req')
    params = {
        'title': 'カーシェアオーナー情報変更',
        'id': num,
        'form': HostUserForm(instance=obj),
    }
    return render(request, 'owners_req/edit.html', params)

def delete(request, num):
    owners_req = HostUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        owners_req.delete()
        return redirect(to='/owners_req')
    params = {
        'title': 'カーシェアオーナー削除',
        'id': num,
        'data': owners_req,
    }
    return render(request, 'owners_req/delete.html', params)


class CreateCarView(TemplateView):
    def __init__(self):
        self.params = {
        'title': '車情報登録',
        'form': CarInfoForm(),
    }
    def get(self, request):
        return render(request, 'owners_req/createCar.html', self.params)
    def post(self, request):
        obj = CarInfoModel()
        owners = CarInfoForm(request.POST, instance=obj)
        owners.save()
        return redirect(to='/owners_req')

