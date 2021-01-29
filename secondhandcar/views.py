from django.shortcuts import render, redirect
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
    params = {
        'title': "価格予測推移グラフ一覧"
    }

    path = "./data/price/price.json"
    with open(path, 'r') as f:
        json_data = f.read()
        json_object = json.loads(json_data)
    car_name = {}
    for price_data in json_object:
        car_id = list(price_data.keys())
        price_dict = list(price_data.values())
        # print(car_id[0])
        # print(price_dict[0])
        params['id_'+str(car_id[0])] = json.dumps(price_dict[0])
        car_data = SecondHandCarInfoModel.objects.get(second_hand_car_id_id=car_id[0])
        car_name['id_'+str(car_id[0])] = car_data.category + '(' + car_data.parent_category + ')'
    # print(car_name)
    params['car_name'] = car_name
        
    return render(request, 'secondhandcar/price.html', params)

def importCSV(request):
    # SecondHandCarAIModel作成
    with open('./data/car_csv/secondhandcar-record.csv') as f:
        reader = csv.reader(f)
        record_list = []
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
                record_list.append(record)
                # record.save()
        SecondHandCarAIModel.objects.bulk_create(record_list)
    
    # SecondHandCarInfoModel作成
    count = -1
    with open('./data/car_csv/used_car_data.csv') as f:
        reader = csv.reader(f)
        record_list = []
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
                record_list.append(record)
                #record.save()
            count += 1
        SecondHandCarInfoModel.objects.bulk_create(record_list)
    
    # SecondHandCarPriceModel作成
    count = 0
    with open('./data/car_csv/car_value_data.csv') as f:
        reader = csv.reader(f)
        record_list = []
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
                    record_list.append(record)
                    # record.save()
            count += 1
        SecondHandCarPriceModel.objects.bulk_create(record_list)
    return redirect(to='secondhandcar:search')


def exportCSV(request):
    # 月１処理とcsv作成
    filename = './data/car_csv/reco_car_data.csv'
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
        path = './data/recommend/user_' + str(ut) + '.json'
        with open(path, 'w') as f:
            f.write(json_data)
        # おすすめAI起動
        recoai.RecommendAI('user_' + str(ut) + '.json')
        # 作成されたjsonファイルをimport
        data = importRecoJson('./data/recommend/reco_user_' + str(ut) + '.json', str(ut))

        secondhandcar_list = setSecondHandCarList(data)
        # ゲストデータを削除
        os.remove('./data/recommend/reco_user_' + str(ut) + '.json')

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
        data = importRecoJson('./data/recommend/reco_user_' + str(request.session['user_id']) + '.json', str(request.session['user_id']))

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
        'title': '中古車詳細',
        'car_obj1': car_obj1,
        'car_obj2': car_obj2
    }
    path = "./data/price/price.json"
    with open(path, 'r') as f:
        json_data = f.read()
        json_object = json.loads(json_data)
    car_name = {}
    for price_data in json_object:
        car_id = list(price_data.keys())
        price_dict = list(price_data.values())
        if car_id[0] == str(num):
            params["price"] = json.dumps(price_dict[0])
    return render(request, 'secondhandcar/detail.html', params)


def search(request, num=1):
    p_c_list0 = ['トヨタ', '日産', 'スズキ', 'ホンダ', 'マツダ', 'ダイハツ','スバル', '三菱', 'ミニ', 'レクサス', 'ジープ', 'ＢＭＷ','アルファ\u3000ロメオ', 'シトロエン', 'フォルクスワーゲン',  'ボルボ', 'ポルシェ', 'メルセデス・ベンツ', 'メルセデスＡＭＧ']  
    if (request.method == 'POST'):
        secondhandcar_info = list(SecondHandCarInfoModel.objects.filter(parent_category=request.POST['parent_category']).values())
        # parent_category_list = list(SecondHandCarInfoModel.objects.order_by('parent_category').distinct('parent_category').values('parent_category'))
        # for item in parent_category_list:
        #     p_c_list.append(item['parent_category'])
        # p_c_list.sort()
        for index in secondhandcar_info:
            index['id'] = str(int(index['id']) - 1)
        params = {
            'title': '中古車',
            'secondhandcar_info': secondhandcar_info,
            'p_c_list0': p_c_list0,
            'POST': True
        }
    else:
        secondhandcar_info = list(SecondHandCarInfoModel.objects.values())
        # parent_category_list = list(SecondHandCarInfoModel.objects.order_by('parent_category').distinct('parent_category').values('parent_category'))
        # p_c_list = []
        # for item in parent_category_list:
        #     p_c_list.append(item['parent_category'])
        # p_c_list.sort()
        for index in secondhandcar_info:
            index['id'] = str(int(index['id']) - 1)
        page = Paginator(secondhandcar_info, 5)
        params = {
            'title': '中古車',
            'secondhandcar_info': page.get_page(num),
            'p_c_list0': p_c_list0,
            'POST': False
        }
    return render(request, 'secondhandcar/search.html', params)



def test(request):
# def priceAImakeJson():
    path = './data/car_csv/car_value_result/'
    files = os.listdir(path)
    files.pop(0)
    print(files)
    add_list = []
    for csvfile in files:
        csvpath = path + csvfile
        tmp_dict = makepriceJson(csvpath)
        add_dict = {}
        index = csvfile[3:5]
        add_dict[int(index)] = tmp_dict
        add_list.append(add_dict)
        

    json_data = json.dumps(add_list, sort_keys=True, indent=4)
    # print(json_data)
    # ファイルを開く(上書きモード)
    path = "./data/price/price.json"
    os.remove(path)
    with open(path, 'w') as f:
        # jsonファイルの書き出し
        f.write(json_data)

def makepriceJson(path):
    tmp_dict = {}
    with open(path) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            tmp_dict[row[0]] = float(row[1])
    return tmp_dict
