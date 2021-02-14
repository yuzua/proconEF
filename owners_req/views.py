from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import HostUserModel, CarInfoModel, ParentCategory, Category, CarInfoParkingModel, CarsharingDateModel, Category
from carsharing_req .models import CarsharUserModel
from parking_req .models import ParkingUserModel
from .forms import HostUserForm, CarInfoForm, CarOptionForm, CarInfoParkingForm, ParkingLoaningForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.views import generic
import datetime
import json, ast
from django.db.models import Q
from parking_booking .models import ParkingBookingModel
from carsharing_booking .models import BookingModel
from django.db import connection



def index(request):
    return HttpResponse("Hello, world. You're at the owners_req index.")



class CreateView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'カーシェアリングオーナー申請',
            'message': '',
            'form': HostUserForm(),
            'data': '',
            'banks': '',
        }
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index') 
        else:
            owner_list = HostUserModel.objects.filter(user_id=request.session['user_id'])
            if owner_list.first() is None:
                banks = [
                    {'name': '三井住友銀行', 'code': '0009'},
                    {'name': '三菱ＵＦＪ銀行', 'code': '0005'},
                    {'name': 'みずほ銀行', 'code': '0001'},
                    {'name': 'ゆうちょ銀行', 'code': '9900'}
                ]
                self.params['banks'] = banks
                # BranchCodeCheck()
                return render(request, 'owners_req/create.html', self.params)
                print(request.user)
        self.params['title'] = 'オーナー情報確認'
        self.params['message'] = 'オーナー情報'
        self.params['data'] = owner_list
        return render(request, 'owners_req/ownerslist.html', self.params)


    def post(self, request):
        banks = [
            {'name': '三井住友銀行', 'code': '0009'},
            {'name': '三菱ＵＦＪ銀行', 'code': '0005'},
            {'name': 'みずほ銀行', 'code': '0001'},
            {'name': 'ゆうちょ銀行', 'code': '9900'}
        ]
        self.params['banks'] = banks
        obj = HostUserModel()
        form = HostUserForm(request.POST, instance=obj)
        self.params['form'] = form
        if form.is_valid():
            bank_code = request.POST['bank_code']
            bank_account_number = request.POST['bank_account_number']
            bank_name = BankCodeCheck(bank_code)
            if "ゆうちょ銀行" == bank_name:
                branch_code = request.POST['branch_code']
                bank_account_number = request.POST['bank_account_number']
                if len(branch_code) != 5:
                    self.params['form'] = form
                    messages.error(self.request, '記号は数字5桁です。')
                    return render(request, 'owners_req/create.html', self.params)
                if len(bank_account_number) != 8:
                    self.params['form'] = form
                    messages.error(self.request, '番号は数字8桁です。')
                    return render(request, 'owners_req/create.html', self.params)
                branch_code = branch_code[1:3] + "8"
                bank_account_number = bank_account_number[:7]
                branch_name = "〇〇支店"
            else:
                if bank_name == False:
                    self.params['form'] = form
                    messages.error(self.request, '銀行コードが不正です。')
                    return render(request, 'owners_req/create.html', self.params)
                branch_code = request.POST['branch_code']
                branch_name = BranchCodeCheck(bank_code, branch_code)
                print(branch_name)
                if branch_name == False:
                    self.params['form'] = form
                    messages.error(self.request, '支店コードが不正です。')
                    return render(request, 'owners_req/create.html', self.params)
                bank_account_number = request.POST['bank_account_number']
            if len(branch_code) != 3:
                self.params['form'] = form
                messages.error(self.request, '支店コードが不正です。')
                return render(request, 'owners_req/create.html', self.params)
            if len(bank_account_number) != 7:
                self.params['form'] = form
                messages.error(self.request, '口座番号は数字7桁です。')
                return render(request, 'owners_req/create.html', self.params)
            
            # 確認画面へ
            data = {
                "bank_code": bank_code,
                "bank_name": bank_name,
                "branch_code": branch_code,
                "branch_name": branch_name,
                "bank_account_number": bank_account_number
            }
            self.params['data'] = data
            return render(request, 'owners_req/checkmember.html', self.params)
        else:
            self.params['form'] = form
            messages.error(self.request, '入力データに問題があります')
            return render(request, 'owners_req/create.html', self.params)
        return render(request, 'owners_req/create.html', self.params)

def checkmember(request):
    if (request.method == 'POST'):
        dt_now = datetime.datetime.now()
        user_id = request.session['user_id']
        day = dt_now
        record = HostUserModel(user_id=user_id, day=day, bank_name=request.POST['bank_name'], bank_code=request.POST['bank_code'], \
            branch_code=request.POST['branch_code'], branch_name=request.POST['branch_name'], bank_account_number=request.POST['bank_account_number'])
        record.save()
        set_flag = CarsharUserModel.objects.get(id=request.session['user_id'])
        set_flag.system_flag += 1
        set_flag.save()
        messages.success(request, '登録完了しました。')
    else:
        messages.error(request, '不正なリクエストです。')
    return redirect(to='/carsharing_req/')


# ----------------------------------------------------------------------------------------------------------------
def BankCodeCheck(num):
    bank_name = None
    path = "./data/bank/bank.json"
    with open(path, 'r') as f:
        json_data = f.read()
    json_data = ast.literal_eval(json_data)['branchdata']
    for bank_data in json_data:
        if bank_data['code'] == num:
            bank_name = bank_data['name']
            break
    if  bank_name:
        return bank_name
    else:
        return False

def BranchCodeCheck(index, num):
    branch_name = None
    print(index)
    if index == "0001" or index == "0005" or index == "0009":
        path = "./data/bank/" + index + ".json"
        print(num)
        with open(path, 'r') as f:
            json_data = f.read()
            json_data = json.loads(json_data)
        for bank_data in list(json_data):
            if bank_data['code'] == num:
                branch_name = bank_data['name']
                break
    else:
        return "〇〇支店"
    if branch_name:
        return branch_name
    else:
        return False

# ----------------------------------------------------------------------------------------------------------------


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
            'form2': CarOptionForm()
        }

    def post(self, request):
        dt_now = datetime.datetime.now()
        day = dt_now
        user_id = request.session['user_id']
        obj = CarInfoModel()
        form = CarInfoForm(request.POST, instance=obj)
        form2 = CarOptionForm(request.POST, instance=obj)
        self.params['form'] = form
        self.params['form2'] = form2
        if form.is_valid() and form2.is_valid():
            car_maker = list(ParentCategory.objects.filter(id=request.POST['parent_category']).values("parent_category"))
            car_model = list(Category.objects.filter(id=request.POST['category']).values("category"))

            # 確認画面へ
            data = {
                "parent_category": request.POST['parent_category'],
                "category": request.POST['category'],
                "license_plate_place": request.POST['license_plate_place'],
                "license_plate_type": request.POST['license_plate_type'],
                "license_plate_how": request.POST['license_plate_how'],
                "license_plate_num": request.POST['license_plate_num'],
                "model_id": request.POST['model_id'],
                "people": request.POST['people'],
                "tire": request.POST['tire'],
                "at_mt": request.POST['at_mt'],
                "babysheet": 'babysheet' in request.POST,
                "car_nav": 'car_nav' in request.POST,
                "etc": 'etc' in request.POST,
                "car_autonomous": 'car_autonomous' in request.POST,
                "around_view_monitor": 'around_view_monitor' in request.POST,
                "non_smoking": 'non_smoking' in request.POST,
                "used_mileage": request.POST['used_mileage'],
                "used_years": request.POST['used_years'],
                "vehicle_inspection_day": request.POST['vehicle_inspection_day']
            }
            self.params['data'] = data
            self.params['car_maker'] = car_maker[0]['parent_category']
            self.params['car_model'] = car_model[0]['category']
            return render(request, 'owners_req/checkcar.html', self.params)
        else:
            messages.error(self.request, '入力データに問題があります')
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

def checkcar(request):
    params = {
        'title': '車情報登録確認画面'
    }
    if (request.method == 'POST'):
        dt_now = datetime.datetime.now()
        day = dt_now
        user_id = request.session['user_id']
        parent_category = ParentCategory.objects.get(id=request.POST['parent_category'])
        category = Category.objects.get(id=request.POST['category'])
        # Str型からBool型に変換
        babysheet = judgmentTF(request.POST['babysheet'])
        car_nav = judgmentTF(request.POST['car_nav'])
        etc = judgmentTF(request.POST['etc'])
        car_autonomous = judgmentTF(request.POST['car_autonomous'])
        around_view_monitor = judgmentTF(request.POST['around_view_monitor'])
        non_smoking = judgmentTF(request.POST['non_smoking'])
        
        record = CarInfoModel(user_id=user_id, parent_category=parent_category, category=category, \
            license_plate_place=request.POST['license_plate_place'], license_plate_type=request.POST['license_plate_type'], \
            license_plate_how=request.POST['license_plate_how'], license_plate_num=request.POST['license_plate_num'], \
            model_id=request.POST['model_id'], people=request.POST['people'], tire=request.POST['tire'], at_mt=request.POST['at_mt'], \
            babysheet=babysheet, car_nav=car_nav, etc=etc, car_autonomous=car_autonomous, around_view_monitor=around_view_monitor, non_smoking=non_smoking, \
            used_mileage=request.POST['used_mileage'], used_years=request.POST['used_years'], \
            vehicle_inspection_day=request.POST['vehicle_inspection_day'], img=request.FILES['img'], day=day)
        record.save()
        if request.session['system_flag'] == 1 or request.session['system_flag'] == 5:
            set_flag = CarsharUserModel.objects.get(id=request.session['user_id'])
            set_flag.system_flag += 2
            set_flag.save()
        messages.success(request, '車両の登録が完了しました。引き続き駐車場情報を追加してください。')
        request.session['info_flag'] = True
        return redirect(to='parking_req:index')
    else:
        messages.error(request, '不正なリクエストです。')
    return redirect(to='/carsharing_req/index')

# ----------------------------------------------------------------------------------------------------------
def judgmentTF(string):
    if string == "True":
        boolean = True
    else:
        boolean = False

    return boolean
# ----------------------------------------------------------------------------------------------------------


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
        params = {
            'title': '車両情報一覧',
            'message': '車両データ',
            'data': car_list, 
        }
        return render(request, 'owners_req/carlist.html', params)    


class SettingInfo(TemplateView):
    def __init__(self):
        self.params = {
            'title':'駐車場、車両情報登録データ',
            'message': '駐車場、車両情報登録データ',
            'car_data': '',
            'parking_data': '',
        }
    def get(self, request):
        exclude_car= []
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
            car_list = CarInfoModel.objects.filter(user_id=request.session['user_id']).exclude(id__in=exclude_car)
            parking_list = ParkingUserModel.objects.filter(user_id=request.session['user_id']).exclude(id__in=exclude_parking)
            self.params['car_data'] = car_list
            self.params['parking_data'] = parking_list
        return render(request, 'owners_req/settinginfo.html', self.params)

    def post(self, request):
        user_id = int(request.POST['user_id'])
        car_id = CarInfoModel.objects.get(id=request.POST['car_id'])
        #car_id = CarInfoModel.POST.get(id=request.POST['car_id'])
        parking_id = ParkingUserModel.objects.get(id=request.POST['parking_id'])
        record = CarInfoParkingModel(user_id=user_id, car_id=car_id, parking_id=parking_id)
        record.save()
        if request.session['system_flag'] <= 7:
            set_flag = CarsharUserModel.objects.get(id=request.session['user_id'])
            set_flag.system_flag += 3
            set_flag.save()
        countflag = False
        print(request.POST['parking_id'])
        ParkingUserModel.objects.filter(id=request.POST['parking_id']).update(countflag = countflag)
        messages.success(self.request, '登録完了しました')
        return redirect(to='/owners_req/createDate')
        #return render(request, 'owners_req/createDate.html', self.params)
    
class CreateDateView(TemplateView):
    def __init__(self):
        self.params = {
            'title': '駐車場/車両一覧',
            'message': '貸出不可能日時を設定してください',
            'form': ParkingLoaningForm(), 
            'car_info': '',  #登録済みの車情報表示
        }
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index')
        else:
            print(request.user)
            car_infos = CarInfoParkingModel.objects.filter(user_id=request.session['user_id']).values("car_id", "parking_id")
            for car_info in car_infos:
                num = CarInfoModel.objects.filter(id=car_info['car_id']).values("category")
                category = Category.objects.filter(id=num[0]['category']).values("category")
                car_info['category'] = category[0]['category']
                address = ParkingUserModel.objects.filter(id=car_info['parking_id']).values("address")
                car_info['address'] = address[0]['address']
            self.params['car_info'] = car_infos
            return render(request, 'owners_req/createDate.html', self.params)
    def post(self, request):
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        request.session['user_car_id'] = request.POST['car_id']

        # POSTデータをdatetime型へ変換
        start = start_day + ' ' + start_time
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M')
        print(start)
        print(type(start))
        end = end_day + ' ' + end_time
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M')
        print(end)
        print(type(end))

        booking_list = BookingModel.objects.filter(car_id=request.session['user_car_id'])
        booking_list = booking_list.filter(Q(start_day=start_day) | Q(start_day=end_day) | Q(end_day=start_day) | Q(end_day=end_day))
        print(booking_list)
        booking_list = booking_list.values('id', 'start_day', 'start_time', 'end_day', 'end_time')
        for item in booking_list:
            booking_id = item['id']
            booking_sd = item['start_day']
            booking_st = item['start_time']
            booking_ed = item['end_day']
            booking_et = item['end_time']
            print('item')
            print(item)
            booking_start = booking_sd + ' ' + booking_st
            booking_start = datetime.datetime.strptime(booking_start, '%Y-%m-%d %H:%M')
            booking_end = booking_ed + ' ' + booking_et
            booking_end = datetime.datetime.strptime(booking_end, '%Y-%m-%d %H:%M')
            if start <= booking_end and end >= booking_start:
                print("被り！！")
                messages.error(request, '申し訳ございません。その時間帯は既に設定済みです。別の車両/駐車場にするか時間帯を変更してください。<br>' \
                     + datetime.datetime.strftime(booking_start, "%Y年%m月%d日 %H:%M") + ' 〜 ' \
                     + datetime.datetime.strftime(booking_end, "%Y年%m月%d日 %H:%M"))
                return render(request, 'owners_req/createDate.html', self.params)
            else:
                print("大丈夫！")

        print(booking_list)

        time = end - start
        d = int(time.days)
        m = int(time.seconds / 60)
        print(d)
        print(int(m))
        times = ''

        if d <= 0:
            print('1day')
        else:
            print('days')
            times = str(d) + '日 '

        if start_time < end_time:
            print('tule')
            h = int(m / 60)
            m = int(m % 60)
            x = str(h) + '時間 ' + str(m) + '分'
            times += x
        elif start_time >= end_time and d < 0:
            print('false')
            obj = BookingModel()
            p_b = ParkingLoaningForm(request.POST, instance=obj)
            self.params['form'] = p_b
            messages.error(request, '終了時刻が開始時刻よりも前です。')
            parking_obj = ParkingUserModel.objects.filter(user_id=request.session['user_id'], countflag=True)
            self.params['parking_obj'] = parking_obj
            return render(request, 'owners_req/createDate.html', self.params)
        else:
            h = int(m / 60)
            m = int(m % 60)
            x = str(h) + '時間 ' + str(m) + '分'
            times += x
        
        charge = -1
        data = {
            'start_day': start_day,
            'start_time': start_time,
            'end_day': end_day,
            'end_time': end_time,
            'charge': charge,
        }
        self.params['kingaku'] = charge
        self.params['data'] = data
        self.params['times'] = times
        self.params['message'] = '情報確認'
        messages.warning(self.request, 'まだ貸し出し不可能日時登録を完了しておりません。<br>こちらの内容で宜しければ確定ボタンをクリックして下さい。')
        return render(request, "owners_req/check.html", self.params)
        
def check(request):
    user_id = int(request.session['user_id'])
    car_id = int(request.session['user_car_id'])
    start_day = request.POST['start_day']
    end_day = request.POST['end_day']
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    charge = int(request.POST['charge'])
    record = BookingModel(user_id = user_id, car_id = car_id, start_day = start_day, \
        end_day = end_day, start_time = start_time, end_time = end_time, charge = charge)
    record.save()
    messages.success(request, '登録が完了しました。')
    del request.session['user_car_id']
    return redirect(to='owners_req:createDate')


# 作業用
def AAA():
    mylist=["支店名","削除","コード"]
    add_list = []
    my_dict = {}
    for num in range(len(my_list)):
        if num % 3 == 0:
            my_dict['name'] = my_list[num]
        if num % 3 == 2:
            my_dict['code'] = my_list[num]

        if num % 3 == 2:
                add_list.append(my_dict)
                my_dict = {}
    
    print(add_list)
    json_data = json.dumps(add_list, sort_keys=True, indent=4)

    # ファイルを開く(上書きモード)
    path = "./data/bank/0001.json"
    with open(path, 'w') as f:
        # jsonファイルの書き出し
        f.write(json_data)

