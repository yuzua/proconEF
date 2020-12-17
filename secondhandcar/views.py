from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.


def index(request):
    purius = {
        "2018-01-01": 197.50772153703286,
        "2018-02-01": 198.3735075655772,
        "2018-03-01": 197.62041918786682,
        "2018-04-01": 195.4252247313193,
        "2018-05-01": 192.51269227496545,
        "2018-06-01": 191.675709700336,
        "2018-07-01": 189.83673273608207,
        "2018-08-01": 184.10639726985875,
        "2018-09-01": 186.42718996612572,
        "2018-10-01": 187.64614565897395,
        "2018-11-01": 188.93014878434968,
        "2018-12-01": 198.6099954901022,
        "2019-01-01": 197.69285425516185,
        "2019-02-01": 198.51602678593534,
        "2019-03-01": 197.89670967901367,
        "2019-04-01": 196.08903984125516,
        "2019-05-01": 192.85596447367732,
        "2019-06-01": 191.97446150719398,
        "2019-07-01": 190.1323541048777,
        "2019-08-01": 184.5016444035261,
        "2019-09-01": 186.66765129489627,
        "2019-10-01": 187.68464853658608,
        "2019-11-01": 189.11827554817046,
        "2019-12-01": 198.6913102704601,
        "2020-01-01": 197.7494995482293,
        "2020-02-01": 198.58214219310483,
        "2020-03-01": 197.95920413523086,
        "2020-04-01": 196.15317582011792,
        "2020-05-01": 192.91993393057805,
        "2020-06-01": 192.03874847413343,
        "2020-07-01": 190.1967779272429,
        "2020-08-01": 184.56676933220345,
        "2020-09-01": 186.73250647742043,
        "2020-10-01": 187.7493875456069,
        "2020-11-01": 189.18284229876218,
        "2020-12-01": 198.75473966537518
    }
    minimini = {
        "2018-01-01": 240.13165570938907,
        "2018-02-01": 229.70751809188445,
        "2018-03-01": 229.27128558773651,
        "2018-04-01": 225.55571198737346,
        "2018-05-01": 218.69309600502197,
        "2018-06-01": 216.55965621223683,
        "2018-07-01": 213.7428197482491,
        "2018-08-01": 218.0727031818359,
        "2018-09-01": 230.02489514194227,
        "2018-10-01": 235.2364055298935,
        "2018-11-01": 245.44470985586253,
        "2018-12-01": 235.59938025382976,
        "2019-01-01": 240.13875510660682,
        "2019-02-01": 229.98085031385148,
        "2019-03-01": 230.09903400787468,
        "2019-04-01": 225.8233025205727,
        "2019-05-01": 218.86055597491776,
        "2019-06-01": 217.1405801595114,
        "2019-07-01": 214.01869453933952,
        "2019-08-01": 218.60525683436973,
        "2019-09-01": 230.0873251343695,
        "2019-10-01": 235.19491847981004,
        "2019-11-01": 245.6769138154912,
        "2019-12-01": 235.70834790001075,
        "2020-01-01": 240.23895161117008,
        "2020-02-01": 230.0878679967908,
        "2020-03-01": 230.20562527707162,
        "2020-04-01": 225.93220856604492,
        "2020-05-01": 218.9730689190929,
        "2020-06-01": 217.25399419099938,
        "2020-07-01": 214.1337339284483,
        "2020-08-01": 218.71790685025144,
        "2020-09-01": 230.193992783386,
        "2020-10-01": 235.2989250256617,
        "2020-11-01": 245.77545910840684,
        "2020-12-01": 235.81208693986758
    }
    params = {
        'purius_json': json.dumps(purius),
        'minimini_json': json.dumps(minimini),
    }
    return render(request, 'secondhandcar/index.html', params)