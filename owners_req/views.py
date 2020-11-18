from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import HostUserModel, CarInfoModel, ParentCategory, Category
from .forms import HostUserForm
from django.views.generic import TemplateView

from django.views import generic
from .forms import CarInfoForm
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
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            return redirect(to='/carsharing_req/index')
        else:
            print(request.user)
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
        record = HostUserModel(user_id = user_id, pay = pay, day = day, bank_name = bank_name, bank_code = bank_code, bank_account_number = bank_account_number, QR_id = QR_id)
        obj = HostUserModel()
        form = HostUserForm(request.POST, instance=obj)
        self.params['form'] = form
        if (form.is_valid()):
            record.save()
            return redirect(to='owners_req:index')
        else:
            self.params['message'] = '入力データに問題があります'
        return render(request, 'owners_req/create.html', self.params)

    
def edit(request):
    params = {
         'title': 'カーシェアオーナー情報変更',
         'id': user_id,
         'message':'',
         'form': HostUserForm(instance=obj),
     
    }
    if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = CarInfoModel.objects.get(id=num)
        form = CarInfoForm(request.POST, instance=obj)
        if (form.is_valid()):
            form.save()
            return redirect(to='/parking_req')
        else:
            params['message'] = '入力データに問題があります'       
    return render(request, 'owners_req/edit.html', params)
    # obj = HostUserModel.objects.get(id=user_id)
    # params = {
    #     'title': 'カーシェアオーナー情報変更',
    #     'id': user_id,
    #     'message':'',
    #     'form': HostUserForm(instance=obj),
    # }
    # if (request.method == 'POST'):
    #     form = HostUserForm(request.POST, instance=obj)
    #     params['form'] = form
    #     if (form.is_valid()):
    #         form.save()
    #         return redirect(to='owners_req:index')
    #     else:
    #         params['message'] = '入力データに問題があります'
    # return render(request, 'owners_req/edit.html', params)


    # obj = HostUserModel.objects.get(id=num)
    # if (request.method == 'POST'):
    #     owners2 = HostUserForm(request.POST, instance=obj)
    #     owners2.save()
    #     return redirect(to='/owners_req')
    # params = {
    #     'title': 'カーシェアオーナー情報変更',
    #     'id': num,
    #     'form': HostUserForm(instance=obj),
    # }
    # return render(request, 'owners_req/edit.html', params)

def delete(request, num):
    owners_req = HostUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        owners_req.delete()
        return redirect(to='/owners_req')
    params = {
        'title': 'カーシェアオーナー削除',
        'id': num,
        'obj': owners_req,
    }
    return render(request, 'owners_req/delete.html', params)


class CreateCarView(TemplateView):
    def __init__(self):
        self.params = {
            'parentcategory_list': list(ParentCategory.objects.all()),
            'category_set': list(Category.objects.all().values()),
            'title': '車情報登録',
            'form': CarInfoForm(),
        }

    def post(self, request):
        
        dt_now = datetime.datetime.now()
        user_id = request.session['user_id']
        # parent_category = request.POST['parent_category']
        # category = request.POST['category']
        day = dt_now
        # license_plate = request.POST['license_plate']
        # model_id = request.POST['model_id']
        # custom = request.POST['custom']
        # people = request.POST['people']
        # tire = request.POST['tire']
        # used_years = request.POST['used_years']
        # vehicle_inspection_day = request.POST['vehicle_inspection_day']

        # parent_category = ParentCategory.objects.get(id=parent_category)
        # CarInfoModel.parent_category = parent_category
        # category = Category.objects.get(id=category)
        # CarInfoModel.category = category

        record = CarInfoModel(user_id = user_id, day = day)
      
        # record = CarInfoModel(user_id = user_id, parent_category = parent_category, \
        #             category = category, day = day, license_plate = license_plate, model_id = model_id,\
        #             custom = custom, people = people, tire = tire, used_years = used_years,\
        #             vehicle_inspection_day = vehicle_inspection_day)
        form = CarInfoForm(request.POST, instance=record)
        
        self.params['form'] = form
        if (form.is_valid()):
            record.save()
            return redirect(to='owners_req:index')
        else:
            self.params['message'] = '入力データに問題があります'
        return render(request, 'owners_req/createCar.html', self.params)

        # obj1 = CarInfoModel()
        # form = CarInfoForm(request.POST, instance=obj1)
        # self.params['form'] = form
        # if (form.is_valid()):
        #     form.save()
        #     return redirect(to='owners_req:index')
        # else:
        #     self.params['message'] = '入力データに問題があります'
        # return render(request, 'owners_req/createCar.html', self.params)
        
    def get(self, request):
        
        #return render(request, 'owners_req/createCar.html', self.params)
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            return redirect(to='/carsharing_req/index')
        else:
            print(self.params['parentcategory_list'])
            print(self.params['category_set'])
            print(request.user)
        return render(request, 'owners_req/createCar.html', self.params)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context

def editCar(request, num1):
    obj1 = CarInfoModel.objects.get(id=num1)
    if (request.method == 'POST'):
        owners2 = CarInfoForm(request.POST, instance=obj1)
        owners2.save()
        return redirect(to='/owners_req')
    params = {
        'title': '車情報変更',
        'id': num1,
        'form': CarInfoForm(instance=obj1),
    }
    return render(request, 'owners_req/editCar.html', params)

def deleteCar(request, num1):
    owners_req = CarInfoModel.objects.get(id=num1)
    owners_req2 = Category.objects.get(id=num1)
    if (request.method == 'POST'):
        owners_req.delete()
        return redirect(to='/owners_req')
    params = {
        'title': '車情報削除',
        'id': num1,
        'obj1': owners_req,
        'obj2': owners_req2,
    }
    return render(request, 'owners_req/deleteCar.html', params)

def carlist(request):
    car = CarInfoModel.objects.filter(user_id=request.session['user_id']).all()
    if (request.method == 'POST'):
        num = request.POST['obj.id']
        obj = CarInfoModel.objects.get(id=num)
        params = {
        'title': '車情報変更',
        'data': obj,
        'id':num,
        'form': CarInfoForm(instance=obj),
        }
        return render(request, 'owners_req/editCar.html', params)
    else:
        params = {
            'title': '車両一覧表示',
            'message': '',
            'data': car
        }
        return render(request, 'owners_req/carlist.html', params) 
