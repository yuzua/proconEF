from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import SecondHandCarAIModel, SecondHandCarInfoModel, SecondHandCarPriceModel
import json
import csv
import os
import time
import ast
from ai import preprocessing, recoai
# Create your views here.


def price(request):
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
    return render(request, 'secondhandcar/price.html', params)

def importCSV(request):
    # SecondHandCarAIModel作成
    with open('/Django/data/car_csv/secondhandcar-record.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)
            if row[0] != 'carID':
                record = SecondHandCarAIModel()
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
    
    # SecondHandCarInfoModel作成
    count = -1
    with open('/Django/data/car_csv/used_car_data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)
            if count != -1:
                record = SecondHandCarInfoModel()
                record.second_hand_car_id_id = str(count)
                record.parent_category = row[0]
                record.category = row[1]
                record.grade = row[2]
                record.release_period = row[3]
                record.model = row[4]
                record.img1 = row[130]
                record.img2 = row[131]
                record.img3 = row[132]
                record.save()
            count += 1
    
    # SecondHandCarPriceModel作成
    count = 0
    with open('/Django/data/car_csv/car_value_data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            if count == 0:
                car_list = row
                length = len(row)
            else:
                for num in range(1,length):
                    record = SecondHandCarPriceModel()
                    record.second_hand_car_id_id = car_list[num]
                    record.day = row[0]
                    record.price = row[num]
                    record.save()
            count += 1


def exportCSV(request):
    # 月１処理とcsv作成
    filename = '/Django/data/car_csv/reco_car_data.csv'
    second_hand_car = list(SecondHandCarAIModel.objects.all())
    second_hand_car_list = []
    index = ["carID","駆動方式","乗車定員","ドア枚数","エンジン型式","エンジン種類","エンジン区分","環境対策エンジン","総排気量(cc)","過給器","ホイールベース(mm)","車両重量(kg)","最低地上高(mm)","最小回転半径(m)","サスペンション形式前","サスペンション形式後","ブレーキ形式後","使用燃料","燃料タンク容量(L)","エアフィルター","2列目シート","アルミホイール","リアスポイラー","フロントフォグランプ","ETC","助手席エアバッグ","サイドエアバッグ","カーテンエアバッグ","頸部衝撃緩和ヘッドレスト","EBD付ABS","セキュリティアラーム","マニュアルモード","チップアップシート","ドアイージークローザー","レーンアシスト","車間距離自動制御システム","前席シートヒーター","床下ラゲージボックス","オーディオソース_DVD","ブレーキアシスト","駐車支援システム","防水加工","地上波デジタルテレビチューナー","ソナー","サイドモニター","その他ナビゲーション","インテリジェントAFS","運転席パワーシート","本革シート","AC電源","ステアリングヒーター","リアフォグランプ","レインセンサー","インテリジェントパーキングアシスト","エマージェンシーサービス","フロント両席パワーシート","オーディオソース_HDD","ニーエアバッグ","ヘッドライトウォッシャー","後退時連動式ドアミラー","VGS/VGRS","ABS","2列目ウォークスルー","3列目シート","電動バックドア","リアエンターテイメントシステム","電気式4WD","HDDナビゲーション","全長(mm)","全幅(mm)","全高(mm)","室内全長(mm)","室内全幅(mm)","室内全高(mm)","マニュアルエアコン","片側スライドドア","最高出力(ps)"]
    second_hand_car_list.append(index)
    for item in second_hand_car:
        item_list = [item.id,item.box_1,item.box_2,item.box_3,item.box_4,item.box_5,item.box_6,item.box_7,item.box_8,item.box_9,item.box_10,item.box_11,item.box_12,item.box_13,item.box_14,item.box_15,item.box_16,item.box_17,item.box_18,item.box_19,item.box_20,item.box_21,item.box_22,item.box_23,item.box_24,item.box_25,item.box_26,item.box_27,item.box_28,item.box_29,item.box_30,item.box_31,item.box_32,item.box_33,item.box_34,item.box_35,item.box_36,item.box_37,item.box_38,item.box_39,item.box_40,item.box_41,item.box_42,item.box_43,item.box_44,item.box_45,item.box_46,item.box_47,item.box_48,item.box_49,item.box_50,item.box_51,item.box_52,item.box_53,item.box_54,item.box_55,item.box_56,item.box_57,item.box_58,item.box_59,item.box_60,item.box_61,item.box_62,item.box_63,item.box_64,item.box_65,item.box_66,item.box_67,item.box_68,item.box_69,item.box_70,item.box_71,item.box_72,item.box_73,item.box_74,item.box_75,item.box_76]
        second_hand_car_list.append(item_list)
    # print(second_hand_car_list)
    # csv作成
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(second_hand_car_list)

    preprocessing.Preprocessing()

def recommend_car(request):
    # ゲストの答えたアンケート(POSTデータ)から提案
    if (request.method == 'POST'):
        # チェックされたアンケート項目を取得
        checks_value = request.POST.getlist('checks[]')
        anser_dict = {}
        # アンケートをjsonファイルへexport
        for anser in checks_value:
            anser_dict[anser] = True
        json_data = json.dumps(anser_dict, sort_keys=True, indent=4)
        ut = int(time.time())
        path = '/Django/data/recommend/user_' + str(ut) + '.json'
        with open(path, 'w') as f:
            f.write(json_data)
        # おすすめAI起動
        recoai.RecommendAI('user_' + str(ut) + '.json')
        # 作成されたjsonファイルをimport
        data = importRecoJson('/Django/data/recommend/reco_user_' + str(ut) + '.json', str(ut))

        secondhandcar_list = setSecondHandCarList(data)
        # ゲストデータを削除
        os.remove('/Django/data/recommend/reco_user_' + str(ut) + '.json')

        params = {
            'secondhandcar_list': secondhandcar_list,
            'title': 'あなたへのおすすめ'
        }
        return render(request, 'secondhandcar/recommend.html', params)

    # 会員か非会員か判定
    if str(request.user) == "AnonymousUser":
        # 非会員は先にアンケートに回答
        survey_list = [
            '乗り心地がいい',
            '荷室の使いやすさ',
            '燃費の良さ',
            '排気量の少なさ',
            '車内空間が広い',
            '静かに走る',
            '馬力がある',
            '乗車定員が多い',
            '小回りが利く',
            '乗車しやすい',
            '安全性能が高い',
            '走行性能が高い',
            '車両サイズが小さい'
        ]
        params = {
            'data': survey_list,
            'message': "あなたが車を選ぶ際に重要視する点を選択して下さい。(複数選択可)",
            'title': "アンケートにお答え下さい"
        }
        return render(request, 'secondhandcar/gestquestionnaire.html', params)
    else:
        # 作成されたjsonデータを使用しておすすめを提案
        data = importRecoJson('/Django/data/recommend/reco_user_' + str(request.session['user_id']) + '.json', str(request.session['user_id']))

    secondhandcar_list = setSecondHandCarList(data)

    params = {
        'secondhandcar_list': secondhandcar_list,
        'title': 'あなたへのおすすめ'
    }
    return render(request, 'secondhandcar/recommend.html', params)



def importRecoJson(path, user_id):
    with open(path, 'r') as f:
            json_data = f.read()
            json_object = json.loads(json_data)
    data = json_object['user_' + user_id]
    return data

def setSecondHandCarList(data):
    one = data['0']
    two = data['1']
    three = data['2']
    four = data['3']
    five = data['4']
    six = data['5']
    one = SecondHandCarInfoModel.objects.get(second_hand_car_id=one)
    two = SecondHandCarInfoModel.objects.get(second_hand_car_id=two)
    three = SecondHandCarInfoModel.objects.get(second_hand_car_id=three)
    four = SecondHandCarInfoModel.objects.get(second_hand_car_id=four)
    five = SecondHandCarInfoModel.objects.get(second_hand_car_id=five)
    six = SecondHandCarInfoModel.objects.get(second_hand_car_id=six)
    secondhandcar_list = [one,two,three,four,five,six]
    return secondhandcar_list


def detail(request, num):
    car_obj1 = SecondHandCarAIModel.objects.get(id=num)
    car_obj2 = SecondHandCarInfoModel.objects.get(second_hand_car_id=num)
    params = {
        'title': '中古車',
        'car_obj1': car_obj1,
        'car_obj2': car_obj2
    }
    return render(request, 'secondhandcar/detail.html', params)


def search(request, num=1):
    if (request.method == 'POST'):
        secondhandcar_info = list(SecondHandCarInfoModel.objects.filter(parent_category=request.POST['parent_category']).values())
        for index in secondhandcar_info:
            index['id'] = str(int(index['id']) - 1)    
        params = {
            'title': '中古車',
            'secondhandcar_info': secondhandcar_info,
            'POST': True
        }
    else:
        secondhandcar_info = list(SecondHandCarInfoModel.objects.values())
        for index in secondhandcar_info:
            index['id'] = str(int(index['id']) - 1)
        page = Paginator(secondhandcar_info, 5)
        params = {
            'title': '中古車',
            'secondhandcar_info': page.get_page(num),
            'POST': False
        }
    return render(request, 'secondhandcar/search.html', params)



def test(request):
    path = "/Django/data/car_csv/car_value_result/"
    files = os.listdir(path)
    files.pop(0)
    print(files)
    for csvfile in files:
        makepriceJson(path, csvfile)

def makepriceJson(fdir, csv):
    path = fdir + csv
    print(path)
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            print(row[0])
            print(row[1])
            tmp_dict = {}
            tmp_dict[row[0]] = row[1]
            print(tmp_dict) 
    