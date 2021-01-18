from django.shortcuts import render, redirect
from .models import CustomUser
from carsharing_req .models import CarsharUserModel
import datetime

# Create your views here.
def check_superuser(request):
    ResetChargeFlag()
    if request.user.id == None:
        return redirect(to='/carsharing_req/index')
    flag = CustomUser.objects.filter(id=request.user.id)
    flag = flag.values('is_superuser')
    flag = flag[0]['is_superuser']
    if flag == True:
        print(request.user)
        return redirect(to='/administrator/')
    else:
        return redirect(to='/carsharing_req/')

def ResetChargeFlag():
    dt_now = datetime.datetime.now()
    d_now = dt_now.strftime('%d')
    if d_now == '01':
        all_user = CarsharUserModel.objects.all()
        if list(all_user)[0].charge_flag == True:
            for user in all_user:
                user.charge_flag = False
                user.save()