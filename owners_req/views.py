from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HostUserModel, CarInfoModel, ParentCategory, Category, CarInfoParkingModel
from carsharing_req .models import CarsharUserModel
from parking_req .models import ParkingUserModel
from .forms import HostUserForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.views import generic
from .forms import CarInfoForm, CarInfoParkingForm
import datetime
import json



def index(request):
    return HttpResponse("Hello, world. You're at the owners_req index.")


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
            messages.error(self.request, 'ログインしてください。')
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
        day = dt_now
        license_plate = request.POST['license_plate']
        record = CarInfoModel(user_id = user_id, day = day, license_plate=license_plate)
        form = CarInfoForm(request.POST, instance=record)
        
        self.params['form'] = form
        if (form.is_valid()):
            record.save()
            messages.success(self.request, '車両の登録が完了しました。引き続き駐車場情報を追加してください。')
            request.session['info_flag'] = True
            return redirect(to='parking_req:index')
        else:
            self.params['message'] = '入力データに問題があります'
        return render(request, 'owners_req/createCar.html', self.params)

        
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
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


def carparkinglist(request):
   
    # user_id = request.session['user_id']
    # #car_id = request.session['car_id']
    # #parking_id = request.session['parking_id']
    # car_id = CarInfoParkingModel.objects.get(car_id=car_id)
    # parking_id = CarInfoParkingModel.objects.get(parking_id=parking_id)
    # obj = CarInfoParkingModel(user_id= user_id, car_id=car_id, parking_id=parking_id)
    # form = CarInfoParkingForm(request.POST, instance=obj)
    # if (form.is_valid()):
    #     record.save()
      
    #     return redirect(to='/owners_req/carparkinglist')

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
            'data_json': json.dumps(data),
            'form': CarInfoParkingForm()
        }
        return render(request, 'owners_req/carparkinglist.html', params)

class SettingInfo(TemplateView):
    def __init__(self):
        self.params = {
            'title':'駐車場、車両情報登録データ',
            'message': '駐車場、車両情報登録データ',
            'car_data': '',
            'parking_data': '',
        }
    def get(self, request):
        exclude_car = []
        exclude_parking = []
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index')
        else:
            set_list = CarInfoParkingModel.objects.filter(user_id=request.session['user_id']).values("car_id", "parking_id")
            for obj in set_list.values("car_id"):
                for index in obj.values():
                    exclude_car.append(index)
            for obj in set_list.values("parking_id"):
                for index in obj.values():
                    exclude_parking.append(index)
            car_list = CarInfoModel.objects.exclude(id__in=exclude_car)
            parking_list = ParkingUserModel.objects.exclude(id__in=exclude_parking)
            self.params['car_data'] = car_list
            self.params['parking_data'] = parking_list
        return render(request, 'owners_req/test.html', self.params)

    def post(self, request):
        user_id = int(request.POST['user_id'])
        car_id = CarInfoModel.objects.get(id=request.POST['car_id'])
        parking_id = ParkingUserModel.objects.get(id=request.POST['parking_id'])
        record = CarInfoParkingModel(user_id=user_id, car_id=car_id, parking_id=parking_id)
        record.save()
        messages.success(self.request, '登録完了しました')
        return redirect(to='/carsharing_req/index')
    
