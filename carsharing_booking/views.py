from django.shortcuts import render
from django.http import HttpResponse
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
    params = {
        'name': '大原簿記法律専門学校',
        'add': '〒277-0842 千葉県柏市末広町１０−１',
    }
    if (request.method == 'POST'):
        params['add'] = request.POST['add']
    return render(request, "carsharing_booking/map.html", params)