from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .models import HostUserModel, CarInfoModel, ParentCategory, Category
from carsharing_req .models import CarsharUserModel
from .forms import HostUserForm
from django.views.generic import TemplateView

from django.views import generic
from .forms import CarInfoForm, ParkingForm
import datetime
import json



def index(request):
    return HttpResponse("Hello, world. You're at the owners_req index.")

def parkingplace(request):
    if str(request.user) == "AnonymousUser":
            print('ゲスト')
            return redirect(to='/carsharing_req/index')
    else:
        params = {
            'hoge': '',
        }
    return render(request, 'owners_req/parkingplace.html', params)

def test_ajax_response(request):
    input_lat = request.POST.getlist("name_input_lat")
    input_lng = request.POST.getlist("name_input_lng")
    hoge = "lat: "  + input_lat[0] + "lng: " + input_lng[0] + "がセットされました"
    request.session['user_lat'] = input_lat[0]
    request.session['user_lng'] = input_lng[0]

    return HttpResponse(hoge)


class CreateView(TemplateView):
    def __init__(self):
        self.params = {
        'title': 'カーシェアリングオーナー申請',
        'message': '',
        'form': HostUserForm(),
        'data': '',
        }
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            return redirect(to='/carsharing_req/index') 
        else:
            owner_list = HostUserModel.objects.filter(user_id=request.session['user_id'])
            if owner_list.first() is None:
                return render(request, 'owners_req/create.html', self.params)
                print(request.user)
        self.params['title'] = 'オーナー情報確認'
        self.params['message'] = 'オーナー情報'
        self.params['data'] = owner_list
        return render(request, 'owners_req/ownerslist.html', self.params)


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

    
def edit(request):
     if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = HostUserModel.objects.get(id=num)
        form1 = HostUserForm(request.POST, instance=obj)
        params = {
            'title':'オーナー情報変更', 
            'form': HostUserForm(),
            'message':'',
            'id':num,
        }
        if (form1.is_valid()):
            form1.save()
            return redirect(to='/owners_req')
        else:
            params['message'] = '入力データに問題があります'   
            params['form'] = HostUserForm(request.POST, instance= obj)        
     return render(request, 'owners_req/edit.html', params)
    
def delete(request, num):
    owners_req = HostUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        # num = request.POST['p_id']
        owners_req.delete()
        return redirect(to='/owners_req')
    return render(request, 'owners_req/delete.html')

def ownerslist(request):
    owner_list = HostUserModel.objects.filter(user_id=request.session['user_id']).all()
    if (request.method == 'POST'):
        num = request.POST['obj.id']
        num1 = request.POST['command']
        #edit
        if (num1 == 'edit'):
            obj = HostUserModel.objects.get(id=num)
            params = {
            'title':'オーナー情報変更', 
            'form': HostUserForm(instance=obj),
            'message':'',
            'id':num,
            }
            return render(request, 'owners_req/edit.html', params)
        #delete    
        if (num1 == 'delete'):
            delete_owners = HostUserModel.objects.get(id=num)
            params = {
            'title': 'オーナー情報削除',
            'message': '※以下のレコードを削除します。',
            'obj': delete_owners,
            'id': num,
            }
            return render(request, 'owners_req/delete.html', params)
    else:
        #sample
        params = {
            'title': 'オーナー情報確認',
            'message': 'オーナー情報',
            'data': owner_list, 
        }
        return render(request, 'owners_req/ownerslist.html', params) 

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
        license_plate = request.POST['license_plate']
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

        record = CarInfoModel(user_id = user_id, day = day, license_plate=license_plate)
      
        # record = CarInfoModel(user_id = user_id, parent_category = parent_category, \
        #             category = category, day = day, license_plate = license_plate, model_id = model_id,\
        #             custom = custom, people = people, tire = tire, used_years = used_years,\
        #             vehicle_inspection_day = vehicle_inspection_day)
        form = CarInfoForm(request.POST, instance=record)
        
        self.params['form'] = form
        if (form.is_valid()):
            record.save()
            return redirect(to='owners_req:parkingplace')
        else:
            self.params['message'] = '入力データに問題があります'
        return render(request, 'owners_req/createCar.html', self.params)

        
    def get(self, request):
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

def editCar(request):
    if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = CarInfoModel.objects.get(id=num)
        form2 = CarInfoForm(request.POST, instance=obj)
        params = {
            'title':'車情報変更', 
            'form': CarInfoForm(),
            'message': '',
            'id':num,
        }
        if (form2.is_valid()):
            form2.save()
            return redirect(to='/owners_req')
        else:
            params['message'] = '入力データに問題があります'
            params['form'] = CarInfoForm(request.POST, instance= obj)        
    return render(request, 'owners_req/editCar.html', params)

def deleteCar(request, num1):
    owners_req = CarInfoModel.objects.get(id=num1)
    if (request.method == 'POST'):
        owners_req.delete()
        return redirect(to='/owners_req')
    params = {
        'title': '車情報削除',
        'id': num1,
        'obj1': owners_req,
    }
    return render(request, 'owners_req/deleteCar.html', params)

def carlist(request):
    car_list = CarInfoModel.objects.filter(user_id=request.session['user_id']).all()
    if (request.method == 'POST'):
        num = request.POST['obj.id']
        num1 = request.POST['command']
        #edit
        if (num1 == 'editCar'):
            obj = CarInfoModel.objects.get(id=num)
            params = {
            'title':'車情報変更', 
            'form': CarInfoForm(instance=obj),
            'message': '',
            'id':num,
            }
            return render(request, 'owners_req/editCar.html', params)
        #delete    
        if (num1 == 'deleteCar'):
            delete_car = CarInfoModel.objects.get(id=num)
            params = {
            'title': '車情報削除',
            'message': '※以下のレコードを削除します。',
            'obj1': delete_car,
            'id': num,
            }
            return render(request, 'owners_req/deleteCar.html', params)
    else:
        #sample
        params = {
            'title': '車両情報一覧',
            'message': '車両データ',
            'data': car_list, 
        }
        return render(request, 'owners_req/carlist.html', params)    

class ParkingHostCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': '駐車場情報登録',
            'message': '前ページで登録した駐車場情報を入力してください。',
            'form': ParkingForm(),
        }
    
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            return redirect(to='/carsharing_req/index')
        else:
            print(request.user)
            print(request.session['user_lat'])
            print(request.session['user_lng'])

        return render(request, 'owners_req/createParking.html', self.params)


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
            return redirect(to='/owners_req/carparkinglist')
            
        return render(request, 'owners_req/createParking.html', self.params)

def editParking(request):
    
    if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = ParkingUserModel.objects.get(id=num)
        parking = ParkingForm(request.POST, instance=obj)
        params = {
            'title':'ParkingEdittest', 
            'form': ParkingForm(),
            'id':num,
        }
        if (parking.is_valid()):
            parking.save()
            return redirect(to='/owners_req')
        else:
            params['form'] = ParkingForm(request.POST, instance= obj)        
        
    return render(request, 'owners_req/carparking.html', params)

def deleteParking(request, num1):
    parking = ParkingUserModel.objects.get(id=num1)
    if (request.method == 'POST'):
        parking.delete()
        return redirect(to='/owners_req')
    params = {
        'title': '駐車場情報削除',
        'id': num1,
        'obj1': owners_req,
    }
    
    return render(request, 'owners_req/carparkinglist.html')

def carparkinglist(request):
    s_p = ParkingUserModel.objects.filter(user_id=request.session['user_id'])
    s_c = CarInfoModel.objects.filter(user_id=request.session['user_id'])
    sample_parking = s_p.values("id", "user_id", "lat", "lng")
    sample_carinfo = s_c.values("id", "user_id", "license_plate")
    if (request.method == 'POST'):
        num = request.POST['obj.id']
        num1 = request.POST['command']
        #駐車場情報変更
        if (num1 == 'editParking'):
            obj = ParkingUserModel.objects.get(id=num)
            params = {
            'title': '駐車場情報変更',
            'id':num,
            'form': ParkingForm(instance=obj), 
            }
            return render(request, 'owners_req/editParking.html', params)
        #駐車場情報削除
        if (num1 == 'deleteParking'):
            delete_parking = ParkingUserModel.objects.get(id=num)
            params = {
            'title': '駐車場情報削除',
            'message': '※以下のレコードを削除します。',
            'obj': delete_parking,
            'id': num,
            }
            return render(request, 'owners_req/deleteParking.html', params)
        #車両情報変更
        if (num1 == 'editCar'):
            obj = CarInfoModel.objects.get(id=num)
            params = {
            'title':'車情報変更', 
            'form': CarInfoForm(instance=obj),
            'message': '',
            'id':num,
            }
            return render(request, 'owners_req/editCar.html', params)
        #車両情報削除
        if (num1 == 'deleteCar'):
            delete_car = CarInfoModel.objects.get(id=num)
            params = {
            'title': '車情報削除',
            'message': '※以下のレコードを削除します。',
            'obj1': delete_car,
            'id': num,
            }
            return render(request, 'owners_req/deleteCar.html', params)
    else:
        data = CarsharUserModel.objects.get(id=request.session['user_id'])
        print(data.pref01+data.addr01+data.addr02)
        add = data.pref01+data.addr01+data.addr02
        #sample
        markerData = list(sample_parking.all())
        markerData2 = list(sample_carinfo.all())

        data = {
            'markerData': markerData,
            'markerData2': markerData2,
        }
        params = {
            'title': '駐車場、車両情報登録データ',
            'message': '駐車場、車両情報登録データ',
            'data': sample_parking,
            'data2': sample_carinfo,
            'name': '自宅',
            'add': add,
            'data_json': json.dumps(data)
        }
        return render(request, 'owners_req/carparkinglist.html', params)

    # car_list = CarInfoModel.objects.filter(user_id=request.session['user_id']).all()
    # if (request.method == 'POST'):
    #     num = request.POST['obj.id']
    #     num1 = request.POST['command']
    #     #edit
    #     if (num1 == 'editCar'):
    #         obj = CarInfoModel.objects.get(id=num)
    #         params = {
    #         'title':'車情報変更', 
    #         'form': CarInfoForm(instance=obj),
    #         'message': '',
    #         'id':num,
    #         }
    #         return render(request, 'owners_req/editCar.html', params)
    #     #delete    
    #     if (num1 == 'deleteCar'):
    #         delete_car = CarInfoModel.objects.get(id=num)
    #         params = {
    #         'title': '車情報削除',
    #         'message': '※以下のレコードを削除します。',
    #         'obj1': delete_car,
    #         'id': num,
    #         }
    #         return render(request, 'owners_req/deleteCar.html', params)
    # else:
    #     #sample
    #     params = {
    #         'title': '車両情報一覧',
    #         'message': '車両データ',
    #         'data': car_list, 
    #     }
    #     return render(request, 'owners_req/carlist.html', params)    


   