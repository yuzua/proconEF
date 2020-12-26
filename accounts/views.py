from django.shortcuts import render, redirect
from .models import CustomUser

# Create your views here.
def check_superuser(request):
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