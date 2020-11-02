from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CarsharOwnersModel
from .forms import CarsharOwnersCreateForm
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the owners_req index.")

class CreateView(TemplateView):
    def __init__(self):
        self.params = {
        'title': 'カーシェアリング申請',
        'form': CarsharOwnersCreateForm(),
    }
    def get(self, request):
        return render(request, 'owners_req/create.html', self.params)
    def post(self, request):
        obj = CarsharOwnersModel()
        owners = CarsharOwnersCreateForm(request.POST, instance=obj)
        owners.save()
        return redirect(to='/owners_req')
        
    
    


    
def edit(request, num):
    obj = CarsharOwnersModel.objects.get(id=num)
    if (request.method == 'POST'):
        owners2 = CarsharOwnersCreateForm(request.POST, instance=obj)
        owners2.save()
        return redirect(to='/owners_req')
    params = {
        'title': 'カーシェアリング予約変更',
        'id': num,
        'form': CarsharOwnersCreateForm(instance=obj),
    }
    return render(request, 'owners_req/edit.html', params)




def delete(request, num):
    owners_req = CarsharOwnersModel.objects.get(id=num)
    if (request.method == 'POST'):
        owners_req.delete()
        return redirect(to='/owners_req')
    params = {
        'title': 'カーシェアリング予約削除',
        'id': num,
        'data': owners_req,
    }
    return render(request, 'owners_req/delete.html', params)
