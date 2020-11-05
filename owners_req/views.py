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
        'message': '',
        'form': HostUserForm(),
        }
    def get(self, request):
        return render(request, 'owners_req/create.html', self.params)
    def post(self, request):
        if request.method == 'POST':
            obj = HostUserModel()
            form = HostUserForm(request.POST, instance=obj)
            self.params['form'] = form
            if (form.is_valid()):
                self.params['message'] = '問題ありません'
                return render(request, 'owners_req/create.html', self.params)
            else:
                self.params['message'] = '入力データに問題があります'
        return render(request, 'owners_req/index.html', self.params)

    
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
        owners3 = CarInfoForm(request.POST, instance=obj)
        owners3.save()
        return redirect(to='/owners_req')

def editCar(request, num1):
    obj = CarInfoModel.objects.get(id=num1)
    if (request.method == 'POST'):
        owners4 = CarInfoForm(request.POST, instance=obj)
        owners4.save()
        return redirect(to='/owners_req')
    params = {
        'title': '車情報変更',
        'id': num1,
        'form': CarInfoForm(instance=obj),
    }
    return render(request, 'owners_req/editCar.html', params)

def deleteCar(request, num1):
    owners_req = CarInfoModel.objects.get(id=num1)
    if (request.method == 'POST'):
        owners_req.delete()
        return redirect(to='/owners_req')
    params = {
        'title': '車情報削除',
        'id': num1,
        'data': owners_req,
    }
    return render(request, 'owners_req/deleteCar.html', params)



