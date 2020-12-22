from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from .models import CarsharUserModel, UsageModel
from .forms import CarsharUserCreateForm, CarsharUserNameForm
from accounts .models import CustomUser
from parking_req .models import *
from owners_req .models import HostUserModel
from carsharing_booking .models import BookingModel
from parking_booking .models import ParkingBookingModel
import json, datetime, hashlib
from django.core.mail import EmailMessage

# Create your views here.

# ゲスト/ユーザ 判定
def index(request):
    querySet = CarsharUserModel.objects.filter(email__contains = request.user.email)
    if querySet.first() is None:
        print('no data')
        return redirect(to='carsharing_req:create')
    if str(request.user) == "AnonymousUser":
        print('ゲスト')
    else:
        print(request.user.email)
    return redirect(to='carsharing_req:set_session')

# user_idをSESSIONに格納・オーナー登録済か判定用flagをSESSIONに格納
def set_session(request):
    data = CarsharUserModel.objects.get(email=request.user.email)
    request.session['user_id'] = data.id
    paking_data = ParkingUserModel.objects.filter(user_id=data.id)
    if paking_data.first() is None:
        request.session['parking_flag'] = False
    else:
        request.session['parking_flag'] = True

    owner_data = HostUserModel.objects.filter(user_id=data.id)
    if owner_data.first() is None:
        request.session['owner_flag'] = False
    else:
        request.session['owner_flag'] = True
    check_usage_obj = checkUsage(request.session['user_id'])
    if check_usage_obj == None:
        print('ok')
    else:
        surveyMail(request, check_usage_obj)
        saveUsage(request, check_usage_obj)

    return redirect(to='carsharing_req:index')


# 説明ページ(HTML)ルーティング
def pages(request, num, page):
    if num == 1:
        if page == 0:
            return render(request, 'page/user_car.html')
        elif page == 1:
            return render(request, 'page/user_car_1.html')
        elif page == 3:
            return render(request, 'page/user_car_3.html')
    elif num == 2:
        return render(request, 'page/user_parking.html')
    elif num == 3:
        return render(request, 'page/owner_car.html')
    elif num == 4:
        return render(request, 'page/owner_parking.html')
    elif num == 0:
        pass
    else:
        return redirect(to='carsharing_req:index')


class CarsharUserInfo(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello World!',
            'message': 'Not found your data.<br>Please send your profile.',
            'form': CarsharUserCreateForm(),
            'link': 'other',
        }
    
    def get(self, request):
        if str(request.user) == "AnonymousUser":
            print('ゲスト')
        else:
            print(request.user)
        # return render(request, 'carsharing_req/index.html', self.params)
        return render(request, 'carsharing_req/top.html', self.params)
    
    def post(self, request):
        msg = 'Your name is <b>' + request.POST['name'] + \
            '(' + request.POST['age'] + \
            ')</b><br>Your mail address is <b>' + request.POST['email'] + \
            '</b><br>Thank you send to me!'
        self.params['message'] = msg
        self.params['form'] = CarsharUserCreateForm(request.POST)
        return render(request, 'carsharing_req/index.html', self.params)

def carsharuserdata(request):
    data = CarsharUserModel.objects.get(id=request.session['user_id'])
    data2 = CustomUser.objects.get(email=request.user.email)
    params = {
        'title': '個人登録情報確認',
        'message': 'ユーザ情報',
        'data': data,
        'data2': data2,
    }
    return render(request, 'carsharing_req/userdata.html', params)


# class CarsharUserSendMail(generic.FormView):

#     template_name = "carsharing_req/index.html"
#     form_class = CarsharUserCreateForm
#     success_url = reverse_lazy('carsharing_req:index')


#     def form_valid(self, form):
#         form.send_email()
#         messages.success(self.request, 'メッセージを送信しました。')
#         return super().form_valid(form)



class CreateView(TemplateView):
    def __init__(self):
        self.params = {
        'title': '会員登録',
        'form': CarsharUserCreateForm(),
        'form_name': CarsharUserNameForm()
    }

    def post(self, request):
        form = CarsharUserCreateForm(request.POST, request.FILES)
        form_name = CarsharUserNameForm(request.POST, request.FILES)

        if form.is_valid() and form_name.is_valid():
            email = request.user.email
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            first_ja = request.POST['first_ja']
            last_ja = request.POST['last_ja']
            gender = 'gender' in request.POST
            birthday_str = birthdayCheck(request.POST['birthday_year'], request.POST['birthday_month'], request.POST['birthday_day'])
            birthday = birthdaySet(birthday_str)
            age = calcAge(birthday_str)

            # 二十歳未満の利用を制限
            if age < 20:
                self.params['form'] = form
                self.params['form_name'] = form_name
                messages.error(self.request, '20歳未満の方はご利用いただけません。')
                return render(request, 'carsharing_req/create.html', self.params)
            if age > 80:
                self.params['form'] = form
                self.params['form_name'] = form_name
                messages.error(self.request, '80歳以上の方はご利用いただけません。')
                return render(request, 'carsharing_req/create.html', self.params)

            zip01 = request.POST['zip01']
            pref01 = request.POST['pref01']
            addr01 = request.POST['addr01']
            addr02 = request.POST['addr02']
            tel = request.POST['tel']
            credit_card_company = request.POST['credit_card_company']
            first_en = request.POST['first_en']
            last_en = request.POST['last_en']
            SECRET_KEY = request.POST['credit_card_num']
            credit_card_num = hashlib.sha256(SECRET_KEY.encode()).hexdigest()
            credit_card_num_check = request.POST['credit_card_num'][13:]
            valid_thru = request.POST['valid_thru']

            dt_now = datetime.datetime.now()
            if 0 >= int(valid_thru[:2]) or int(valid_thru[:2]) > 12:
                self.params['form'] = form
                self.params['form_name'] = form_name
                messages.error(self.request, 'クレジットカードの期限が不正です。')
                return render(request, 'carsharing_req/create.html', self.params)
            dt_now_y = str(dt_now.year)[:2]
            if int(dt_now_y) > int(valid_thru[3:]):
                self.params['form'] = form
                self.params['form_name'] = form_name
                messages.error(self.request, 'クレジットカードの有効期限が切れています。')
                return render(request, 'carsharing_req/create.html', self.params)
            elif int(dt_now_y) == int(valid_thru[3:]) and int(valid_thru[:2]) < dt_now.month:
                self.params['form'] = form
                self.params['form_name'] = form_name
                messages.error(self.request, 'クレジットカードの有効期限が切れています。')
                return render(request, 'carsharing_req/create.html', self.params)
            # dt_now = datetime.datetime.now()
            # dt_now.year()
            # if int(valid_thru[3:])

            SECRET_KEY = request.POST['security_code']
            security_code = hashlib.sha256(SECRET_KEY.encode()).hexdigest()
            plan = request.POST['plan']
            img = request.FILES['img']
            record = CarsharUserModel(email=email, first_name=first_name, last_name=last_name, first_ja=first_ja, last_ja=last_ja, \
                gender=gender, age=age, birthday=birthday, zip01=zip01, pref01=pref01, addr01=addr01, addr02=addr02, tel=tel, \
                credit_card_company=credit_card_company, first_en=first_en, last_en=last_en, \
                credit_card_num=credit_card_num, credit_card_num_check=credit_card_num_check, valid_thru=valid_thru, \
                security_code=security_code, plan=plan, img=img)
            record.save()
            messages.success(request, '会員登録が完了しました。')
        else:
            self.params['form'] = form
            self.params['form_name'] = form_name
            return render(request, 'carsharing_req/create.html', self.params)
        return redirect(to='carsharing_req:first')
        
    def get(self, request):
        dt_now = datetime.datetime.now()
        min_year, max_year = LimitationAge(dt_now)
        self.params['min_year'] = min_year
        self.params['max_year'] = max_year
        querySet = CarsharUserModel.objects.filter(email__contains = request.user.email)
        if querySet.first() is None:
            print('no data')
            messages.info(self.request, '会員登録して下さい。')
        else:
            print('data　exist')
            return redirect(to='carsharing_req:index')
        return render(request, 'carsharing_req/create.html', self.params)

# -------------------------------------------------------------------------------------------------------
# 年齢制限
def LimitationAge(dt_now):
    min_year = dt_now.year - 20
    max_year = dt_now.year - 80
    return min_year, max_year

# 生年月日
def birthdayCheck(y, m, d):
    if len(m) == 1:
        m = '0' + m
    if len(d) == 1:
        d = '0' + d
    birthday = y + m + d
    return birthday

# 生年月日設定(型変換)
def birthdaySet(ymd):
    y = ymd[0:4]
    m = ymd[4:6]
    d = ymd[6:8]
    tstr = y + '-' + m + '-' + d
    tdatetime = datetime.datetime.strptime(tstr, '%Y-%m-%d')
    return tdatetime

# 年齢計算関数
def calcAge(birthdayStr):
  if not (birthdayStr.isdigit() and len(birthdayStr)==8):
    return -1
  dStr = datetime.datetime.now().strftime("%Y%m%d")
  return (int(dStr)-int(birthdayStr))//10000
# -------------------------------------------------------------------------------------------------------


class CalendarView(TemplateView):
    def __init__(self):
        self.params = {
        'title': 'FullCalendar',
        'events': ''
    }

    def get(self, request):
        # カーシェアリング予約
        events = []
        booking = BookingModel.objects.filter(user_id=request.session['user_id']).exclude(charge=-1).order_by('end_day', 'end_time')
        booking = booking.values("id", "start_day", "start_time", "end_day", "end_time")
        for obj in booking:
            title = obj.get("id")
            start = obj.get("start_day") + 'T' + obj.get("start_time")
            end = obj.get("end_day") + 'T' + obj.get("end_time")
            event = dict((['title', 'カーシェアリング予約'+str(title)], ['start', start], ['end', end], ['color', '#9BF9CC']))
            events.append(event)
        
        # 駐車場予約
        booking2 = ParkingBookingModel.objects.filter(user_id=request.session['user_id']).exclude(charge=-1).order_by('end_day', 'end_time')
        booking2 = booking2.values("id", "start_day", "start_time", "end_day", "end_time")
        for obj in booking2:
            title = obj.get("id")
            start = obj.get("start_day") + 'T' + obj.get("start_time")
            end = obj.get("end_day") + 'T' + obj.get("end_time")
            event = dict((['title', '駐車場予約'+str(title)], ['start', start], ['end', end], ['color', '#A7F1FF']))
            events.append(event)
        
        # 車両貸し出し制限
        loaning1 = BookingModel.objects.filter(user_id=request.session['user_id'], charge=-1).order_by('end_day', 'end_time')
        loaning1 = loaning1.values("id", "start_day", "start_time", "end_day", "end_time")
        for obj in loaning1:
            title = obj.get("id")
            start = obj.get("start_day") + 'T' + obj.get("start_time")
            end = obj.get("end_day") + 'T' + obj.get("end_time")
            event = dict((['title', '車両貸し出し'+str(title)], ['start', start], ['end', end], ['color', '#00CC33']))
            events.append(event)


        # 駐車場貸し出し制限
        loaning2 = ParkingBookingModel.objects.filter(user_id=request.session['user_id'], charge=-1).order_by('end_day', 'end_time')
        loaning2 = loaning2.values("id", "start_day", "start_time", "end_day", "end_time")
        for obj in loaning2:
            title = obj.get("id")
            start = obj.get("start_day") + 'T' + obj.get("start_time")
            end = obj.get("end_day") + 'T' + obj.get("end_time")
            event = dict((['title', '駐車場貸し出し'+str(title)], ['start', start], ['end', end], ['color', '#6495ED']))
            events.append(event)
        self.params['events'] = json.dumps(events)
        
        return render(request, 'carsharing_req/calendar.html', self.params)


def details(request):
    dt_now = datetime.datetime.now()
    d_now = dt_now.strftime('%Y-%m-%d')
    booking = BookingModel.objects.filter(user_id=request.session['user_id'], end_day__lt=dt_now).exclude(charge=-1).order_by('-end_day', '-end_time')
    booking2 = ParkingBookingModel.objects.filter(user_id=request.session['user_id'], end_day__lt=dt_now).exclude(charge=-1).order_by('-end_day', '-end_time')
    params = {
        'data': booking,
        'data2': booking2,
    }
    return render(request, 'carsharing_req/details.html', params)





def checkUsage(user_id):
    dt_now = datetime.datetime.now()
    d_now = dt_now.strftime('%Y-%m-%d')
    t_now = dt_now.strftime('%H:%M')
    usage = UsageModel.objects.filter(user_id=user_id).values('booking_id')
    print(usage)
    if len(usage) == 0:
        print('first')
        booking = BookingModel.objects.filter(user_id=user_id, end_day__lte=d_now).exclude(charge=-1).values().order_by('end_day', 'end_time').last()
    else:
        usage_list = []
        for booking_id in usage:
            usage_list.append(booking_id['booking_id'])
            booking = BookingModel.objects.filter(user_id=user_id, end_day__lte=d_now).exclude(id__in=usage_list).exclude(charge=-1).exclude(end_time__gte=t_now).values().order_by('end_day', 'end_time').last()
    print(booking)
    return booking


def surveyMail(request, booking):
    
    subject = "アンケート回答のお願い"
    attachments = "http://127.0.0.1:8000/survey/questionnaire"
    message = str(request.user) + "様\n \
        時間内の返却ありがとうございました。\n \
        またのご利用をお待ちしております。\n\n \
        開始日: " + booking['start_day'] + "\n \
        開始時刻: " + booking['start_time'] + "\n \
        終了日: " + booking['end_day'] + "\n \
        終了時刻: " + booking['end_time'] + "\n \
        料金: " + str(booking['charge']) + "円\n\n \
        アンケートにお答え下さい。\n \
        URL: " + attachments + "\n"
    user = request.user  # ログインユーザーを取得する
    from_email = 'admin@gmail.com'  # 送信者
    user.email_user(subject, message, from_email)  # メールの送信
    pass


def saveUsage(request, booking):
    booking_id = BookingModel.objects.get(id=booking['id'])
    record = UsageModel(user_id=booking['user_id'], car_id=booking['car_id'], \
        booking_id=booking_id, start_day=booking['start_day'], start_time=booking['start_time'], \
        end_day=booking['end_day'], end_time=booking['end_time'], charge=booking['charge'])
    record.save()
    pass