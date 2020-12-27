from django.shortcuts import render
from django.http import HttpResponse
from .models import SecondHandCarModel
import json
import csv
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

def importCSV(request):
    with open('/Django/data/car_csv/secondhandcar-record.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)
            if row[0] != 'carID':
                record = SecondHandCarModel()
                record.id = row[0]
                record.box_1 = row[1]
                record.box_2 = row[2]
                record.box_3 = row[3]
                record.box_4 = row[4]
                record.box_5 = row[5]
                record.box_6 = row[6]
                record.box_7 = row[7]
                record.box_8 = row[8]
                record.box_9 = row[9]
                record.box_10 = row[10]
                record.box_11 = row[11]
                record.box_12 = row[12]
                record.box_13 = row[13]
                record.box_14 = row[14]
                record.box_15 = row[15]
                record.box_16 = row[16]
                record.box_17 = row[17]
                record.box_18 = row[18]
                record.box_19 = row[19]
                record.box_20 = row[20]
                record.box_21 = row[21]
                record.box_22 = row[22]
                record.box_23 = row[23]
                record.box_24 = row[24]
                record.box_25 = row[25]
                record.box_26 = row[26]
                record.box_27 = row[27]
                record.box_28 = row[28]
                record.box_29 = row[29]
                record.box_30 = row[30]
                record.box_31 = row[31]
                record.box_32 = row[32]
                record.box_33 = row[33]
                record.box_34 = row[34]
                record.box_35 = row[35]
                record.box_36 = row[36]
                record.box_37 = row[37]
                record.box_38 = row[38]
                record.box_39 = row[39]
                record.box_40 = row[40]
                record.box_41 = row[41]
                record.box_42 = row[42]
                record.box_43 = row[43]
                record.box_44 = row[44]
                record.box_45 = row[45]
                record.box_46 = row[46]
                record.box_47 = row[47]
                record.box_48 = row[48]
                record.box_49 = row[49]
                record.box_50 = row[50]
                record.box_51 = row[51]
                record.box_52 = row[52]
                record.box_53 = row[53]
                record.box_54 = row[54]
                record.box_55 = row[55]
                record.box_56 = row[56]
                record.box_57 = row[57]
                record.box_58 = row[58]
                record.box_59 = row[59]
                record.box_60 = row[60]
                record.box_61 = row[61]
                record.box_62 = row[62]
                record.box_63 = row[63]
                record.box_64 = row[64]
                record.box_65 = row[65]
                record.box_66 = row[66]
                record.box_67 = row[67]
                record.box_68 = row[68]
                record.box_69 = row[69]
                record.box_70 = row[70]
                record.box_71 = row[71]
                record.box_72 = row[72]
                record.box_73 = row[73]
                record.box_74 = row[74]
                record.box_75 = row[75]
                record.box_76 = row[76]
                record.save()
