from django.shortcuts import render
from django.http import HttpResponse
from carsharing_req .models import CarsharUserModel
# Create your views here.


def test_ajax_app(request):
    if str(request.user) == "AnonymousUser":
        print('ゲスト')
    else:
        print(request.user)
    hoge = "Hello Django!!"

    return render(request, "carsharing_booking/index.html", {
        "hoge": hoge,
    })

def test_ajax_response(request):
    input_text = request.POST.getlist("name_input_text")
    hoge = "Ajax Response: " + input_text[0]

    return HttpResponse(hoge)

def map(request):
    data = CarsharUserModel.objects.get(id=request.session['user_id'])
    print(data.pref01+data.addr01+data.addr02)
    add = data.pref01+data.addr01+data.addr02
    params = {
        'name': '自宅',
        'add': add,
    }
    if (request.method == 'POST'):
        params['add'] = request.POST['add']
    return render(request, "carsharing_booking/map.html", params)