from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django .shortcuts import redirect
from parking_req .models import ParkingUserModel
from carsharing_req .models import CarsharUserModel
from .forms import AdminParkingForm, UploadFileForm
from accounts .models import CustomUser
from owners_req .models import HostUserModel, CarInfoModel, ParentCategory, Category, CarInfoParkingModel
from owners_req .forms import CarInfoForm, CarInfoParkingForm, CarsharingDateForm
from django.contrib import messages
from django.views import generic
import datetime
import json
import openpyxl
import re


# Create your views here.
def check_superuser(request):
    if request.user.id == None:
        return redirect(to='/carsharing_req/index')
    flag = CustomUser.objects.filter(id=request.user.id)
    flag = flag.values('is_superuser')
    flag = flag[0]['is_superuser']
    if flag == True:
        print(request.user)
        return redirect(to='/administrator/index')
    else:
        return redirect(to='/carsharing_req/')

def index(request):
    # データのダウンロード
    # AllCarDownload()
    params = {
        'hoge': '',
    }
    return render(request, 'administrator/index.html', params)


def test_ajax_response(request):
    input_lat = request.POST.getlist("name_input_lat")
    input_lng = request.POST.getlist("name_input_lng")
    hoge = "lat: "  + input_lat[0] + "lng: " + input_lng[0] + "がセットされました"
    request.session['user_lat'] = input_lat[0]
    request.session['user_lng'] = input_lng[0]

    return HttpResponse(hoge)

class ParkingAdminCreate(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'ステーション追加',
            'message': '駐車場情報入力',
            'form': AdminParkingForm(),
        }
    
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index')
        else:
            self.params['lat'] = request.session['user_lat']
            self.params['lng'] = request.session['user_lng']
            return render(request, 'administrator/create.html', self.params)

    def post(self, request):
        dt_now = datetime.datetime.now()
        user_id = 0
        address = request.POST['address']
        lat = request.session['user_lat']
        lng = request.session['user_lng']
        day = dt_now
        parking_type = request.POST['parking_type']
        width = request.POST['width']
        length = request.POST['length']
        height = request.POST['height']
        count = request.POST['count']
        admin = True
        record = ParkingUserModel(user_id = user_id, address = address, lat = lat, lng=lng, day = day, parking_type = parking_type, \
            width = width, length = length, height = height, count = count, admin = admin)
        obj = ParkingUserModel()
        parking = AdminParkingForm(request.POST, instance=obj)
        self.params['form'] = parking
        if (parking.is_valid()):
            record.save()
            del request.session['user_lat']
            del request.session['user_lng']
            if 'info_flag' in request.session:
                print(request.session['info_flag'])
                return redirect(to='/administrator/settinginfo')
            else:
                print('none')
                messages.success(self.request, '駐車場登録が完了しました。')
                return redirect(to='/administrator/admin_main')
        return render(request, 'administrator/create.html', self.params)

def admin_main(request):
    s_p = ParkingUserModel.objects.filter(user_id=0)
    admin_parking = s_p.values("id", "address", "user_id", "lat", "lng")
    if (request.method == 'POST'):
        #num = request.POST['obj.id']
        num1 = request.POST['command']
        #edit
        if (num1 == 'edit'):
            num = request.POST['obj.id']
            obj = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingAdminEdit',
            'message': '駐車場情報修正',
            'id':num,
            'form': AdminParkingForm(instance=obj), 
            }
            return render(request, 'administrator/edit.html', params)
        #delete    
        if (num1 == 'delete'):
            num = request.POST['obj.id']
            delete_parking = ParkingUserModel.objects.get(id=num)
            params = {
            'title': 'ParkingAdminDelete',
            'message': '駐車場情報削除',
            'obj': delete_parking,
            'id': num,
            }
            return render(request, 'administrator/delete.html', params)
        #map
        if (num1 == 'map'):
            # data = CarsharUserModel.objects.get(id=request.session['user_id'])
            # print(data.pref01+data.addr01+data.addr02)
            add = '千葉県柏市末広町10-1'
            markerData = list(admin_parking.all())
            data = {
                'markerData': markerData,
            }
            params = {
            'name': '自宅',
            'add': add,
            'data_json': json.dumps(data)
            }
            if (request.method == 'POST'):
                params['add'] = request.POST['add']
            return render(request, "administrator/admin_main.html", params)    
    else:
        # data = CarsharUserModel.objects.get(id=0)
        # print(data.pref01+data.addr01+data.addr02)
        add = '千葉県柏市末広町10-1'
        #admin_main
        markerData = list(admin_parking.all())
        data = {
            'markerData': markerData,
        }
        params = {
            'title': 'ParkingAdminMain',
            'message': '駐車場登録データ',
            'data': admin_parking,
            'name': '自宅',
            'add': add,
            'data_json': json.dumps(data)
        }
        return render(request, 'administrator/admin_main.html', params)        

def edit(request):
    if (request.method == 'POST'):
        num = request.POST['p_id']
        obj = ParkingUserModel.objects.get(id=num)
        parking = AdminParkingForm(request.POST, instance=obj)
        params = {
            'title':'ParkingAdminEdit',
            'message': '駐車場情報修正', 
            'form': AdminParkingForm(),
            'id':num,
        }
        if (parking.is_valid()):
            parking.save()
            messages.success(request, '駐車場情報を修正しました。')
            return redirect(to='/administrator/admin_main')
        else:
            params['form'] = AdminParkingForm(request.POST, instance= obj)        
        
    return render(request, 'administrator/edit.html', params)

def delete(request, num):
    parking = ParkingUserModel.objects.get(id=num)
    if (request.method == 'POST'):
        parking.delete()
        messages.success(request, '駐車場情報を削除しました。')
        return redirect(to='/administrator/admin_main')

    return render(request, 'administrator/delete.html')

class CreateCarAdminView(TemplateView):
    def __init__(self):
        self.params = {
            'parentcategory_list': list(ParentCategory.objects.all()),
            'category_set': list(Category.objects.all().values()),
            'title': '車情報登録',
            'message': '車情報入力',
            'form': CarInfoForm(),
        }

    def post(self, request):
        dt_now = datetime.datetime.now()
        user_id = 0
        day = dt_now
        license_plate = request.POST['license_plate']
        record = CarInfoModel(user_id = user_id, day = day, license_plate=license_plate)
        form = CarInfoForm(request.POST, instance=record)
        
        self.params['form'] = form
        if (form.is_valid()):
            record.save()
            messages.success(self.request, '車両の登録が完了しました。引き続き駐車場情報を追加してください。')
            request.session['info_flag'] = True
            return redirect(to='/administrator/index')
        else:
            self.params['message'] = '入力データに問題があります'
        return render(request, 'administrator/create.html', self.params)

        
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index')
        else:
            print(self.params['parentcategory_list'])
            print(self.params['category_set'])
            print(request.user)
        return render(request, 'administrator/createCar.html', self.params)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parentcategory_list'] = ParentCategory.objects.all()
        return context                    

class SettingAdminInfo(TemplateView):
    def __init__(self):
        self.params = {
            'title':'駐車場、車両情報登録データ',
            'message': '駐車場、車両情報登録データ',
            'car_data': '',
            'parking_data': '',
            # 'data_json': '',
        }
    def get(self, request):
        exclude_car= []
        exclude_parking = []
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
            messages.error(self.request, 'ログインしてください。')
            return redirect(to='/carsharing_req/index')
        else:
            set_list = CarInfoParkingModel.objects.filter(user_id=0).values("car_id", "parking_id")
            for obj in set_list.values("car_id"):
                for index in obj.values():
                    exclude_car.append(index)
            for obj in set_list.values("parking_id"):
                for index in obj.values():
                    exclude_parking.append(index)
            car_list = CarInfoModel.objects.filter(user_id=0).exclude(id__in=exclude_car)
            # parking_list = ParkingUserModel.objects.filter(user_id=0).exclude(id__in=exclude_parking)
            parking_list = ParkingUserModel.objects.filter(user_id=0, countflag=True)
            self.params['car_data'] = car_list
            self.params['parking_data'] = parking_list
            # item = parking_list.values("id", "user_id", "lat", "lng")
            # item_list = list(item.all())
            # data = {
            #     'markerData': item_list,
            # }
            # self.params['data_json'] = json.dumps(data)
        return render(request, 'administrator/settinginfo.html', self.params)

    def post(self, request):
        user_id = int(request.POST['user_id'])
        car_id = CarInfoModel.objects.get(id=request.POST['car_id'])
        parking_id = ParkingUserModel.objects.get(id=request.POST['parking_id'])
        record = CarInfoParkingModel(user_id=user_id, car_id=car_id, parking_id=parking_id)
        record.save()
        print(request.POST['parking_id'])
        nowint = CarInfoParkingModel.objects.filter(parking_id=request.POST['parking_id']).count()
        maxint = ParkingUserModel.objects.filter(id=request.POST['parking_id']).values_list("count", flat=True)
        if nowint == maxint[0]:
            print('out')
            countflag = False
            ParkingUserModel.objects.filter(id=request.POST['parking_id']).update(countflag = countflag)
        else:
            print('safe')
        print(nowint)
        messages.success(self.request, '登録完了しました')
        return redirect(to='/administrator/admin_main')

class UploadData(TemplateView):
    def __init__(self):
        self.params = {
            'title':'UploadData',
            'data': 'none',
            'form': ''
        }
    def get(self, request):
        form = UploadFileForm()
        self.params['form'] = form
        return render(request, 'administrator/upload_data.html', self.params)
    def post(self, request):
        file_name = request.FILES['file']
        json_data = json.loads(request.POST['output'])
        self.params['data'] = json_data
        if str(file_name)[0] == 'p':
            AllParentCategoryUpload(json_data)
        elif str(file_name)[0] == 'c':
            AllCategoryUpload(json_data)
        else:
            print('error')
            self.params['data'] = 'error'
        return render(request, 'administrator/upload_data.html', self.params)




# -------------------------- DB上に追加保存された全車両のデータをxlsxに書き出し -------------------------- 
def AllCarDownload():
    dt_now = str(datetime.datetime.now())

    # メーカー情報(親カテゴリー)をjsonでダウンロード
    AllParentCategoryDownload(dt_now)
    # 車種情報(子カテゴリー)をjsonでダウンロード
    AllCategoryDownload(dt_now)

    data = [
        ["車両ID","ユーザID","登録日","メーカー","車種","ナンバープレート","型番","カスタム","乗車人数","タイヤ","使用年数","車検予定日"]
    ]
    data_list = list(CarInfoModel.objects.values())
    for data_dict in data_list:
        tmp = list(data_dict.values())
        # datetime型は入力できない為、str型にlist内を全変換：map()
        result = map((lambda x: str(x)), tmp)
        data.append(list(result))

    # ブックの読み込みとシート選択
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]

    # 行ごとに取り出してからExcelへ挿入
    for row in data:
        sheet.append(row)

    # xlsx型式で保存
    file_name = "/Django/data/car_data/" + dt_now + ".xlsx"
    wb.save(file_name)

def AllParentCategoryDownload(dt_now):
    p_c = list(ParentCategory.objects.values())
    json_data = json.dumps(p_c, sort_keys=True, indent=4)

    # ファイルを開く(上書きモード)
    path = "/Django/data/car_data/pc_" + dt_now + ".json"
    with open(path, 'w') as f:
        # jsonファイルの書き出し
        f.write(json_data)

def AllCategoryDownload(dt_now):
    c = list(Category.objects.values())
    json_data = json.dumps(c, sort_keys=True, indent=4)

    # ファイルを開く(上書きモード)
    path = "/Django/data/car_data/c_" + dt_now + ".json"
    with open(path, 'w') as f:
        # jsonファイルの書き出し
        f.write(json_data)
# -------------------------- DB上に追加保存された全車両のデータをxlsxに書き出し -------------------------- 


# --------------------------------- 読み込んだjsonファイルをDBへ格納 ---------------------------------- 
def AllParentCategoryUpload(json_data):
    print(type(json_data))
    for data in json_data:
        print(data['id'])
        print(list(data.keys()))
        print(list(data.values()))
        record = ParentCategory.objects.get(id=data['id'])
        print(record)
        record.parent_category = data['parent_category']
        print(record)
        record.save()

def AllCategoryUpload(json_data):
    print(json_data)
# --------------------------------- 読み込んだjsonファイルをDBへ格納 ---------------------------------- 