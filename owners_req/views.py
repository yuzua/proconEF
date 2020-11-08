from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import HostUserModel
from .forms import HostUserForm
from django.views.generic import TemplateView

from django.views import generic
from .forms import PostCreateForm

import datetime
# from .models import Post, ParentCategory, Category
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
        dt_now = datetime.datetime.now()
        user_id = request.session['user_id']
        pay = request.POST['pay']
        day = dt_now
        bank_name = request.POST['bank_name']
        bank_code = request.POST['bank_code']
        bank_account_number = request.POST['bank_account_number']
        QR_id = request.POST['QR_id']
        record = HostUserModel(user_id = user_id, pay = pay, day = day, \
            bank_name = bank_name, bank_code = bank_code, bank_account_number = bank_account_number, QR_id = QR_id)
        obj = HostUserModel()
        form = HostUserForm(request.POST, instance=obj)
        self.params['form'] = form
        if (form.is_valid()):
            record.save()
            return redirect(to='owners_req:index')
        else:
            self.params['message'] = '入力データに問題があります'
        return render(request, 'owners_req/create.html', self.params)

    
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


class PostCreate(TemplateView):
    def __init__(self):
        self.params = {
            'parentcategory_list': list(ParentCategory.objects.all()),
            'category_set': list(Category.objects.all().values()),
            'title': 'Owner Create',
            'form': PostCreateForm(),
        }

    def post(self, request):
        obj = Post()
        owners = PostCreateForm(request.POST, instance=obj)
        owners.save()
        return redirect(to='carsharing_req:createCar')
        
    def get(self, request):
        print(self.params['parentcategory_list'])
        print(self.params['category_set'])
        return render(request, 'owners_req/createCar.html', self.params)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context


