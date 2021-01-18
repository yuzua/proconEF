def Preprocessing():
    #生データの前処理(毎月1日にDBからデータを出力しAIが読み込める形に変換、csv(jsonファイルとして保持しておく))
    #前処理が終わったら元のデータは削除する
    import pandas as pd
    import numpy as np
    import json
    import os

    #中古車レコメンドAIデータ読み込み(DBから出力されたもの)
    df = pd.read_csv('./data/car_csv/reco_car_data.csv')
    os.remove('./data/car_csv/reco_car_data.csv')
    if os.path.exists('./data/car_csv/car_data.csv'):
        os.remove('./data/car_csv/car_data.csv')

    df = pd.get_dummies(df, columns=['駆動方式','エンジン型式','エンジン種類','エンジン区分','サスペンション形式前','サスペンション形式後','ブレーキ形式後','使用燃料'])
    li = ['エアフィルター','アルミホイール','リアスポイラー','フロントフォグランプ','ETC','助手席エアバッグ','サイドエアバッグ','カーテンエアバッグ','頸部衝撃緩和ヘッドレスト','EBD付ABS','セキュリティアラーム','マニュアルモード','チップアップシート','ドアイージークローザー','レーンアシスト','車間距離自動制御システム','前席シートヒーター','床下ラゲージボックス','オーディオソース_DVD','ブレーキアシスト','駐車支援システム','防水加工','地上波デジタルテレビチューナー','ソナー','サイドモニター','その他ナビゲーション','インテリジェントAFS','運転席パワーシート','本革シート','AC電源','ステアリングヒーター','リアフォグランプ','レインセンサー','インテリジェントパーキングアシスト','エマージェンシーサービス','フロント両席パワーシート','オーディオソース_HDD','ニーエアバッグ','ヘッドライトウォッシャー','後退時連動式ドアミラー','VGS/VGRS','ABS','電動バックドア','リアエンターテイメントシステム','電気式4WD','HDDナビゲーション','マニュアルエアコン','片側スライドドア']

    for i in df:
        if i in li:
            for x in range(len(df)):
                if df[i][x] == '○':
                    df[i][x] = 1
                else:
                    df[i][x] = 0

    df = df.fillna({'環境対策エンジン': 0})
    for i in range(len(df)):
        if df['環境対策エンジン'][i] == 0:
            pass
        else:
            df['環境対策エンジン'][i] = 1

    for i in range(len(df)):
        if df['過給器'][i] == 'ターボ':
            df['過給器'][i] = 1
        else:
            df['過給器'][i] = 0

    for i in range(len(df)):
        if df['2列目シート'][i] == '固定':
            df['2列目シート'][i] = 1
        else:
            df['2列目シート'][i] = 0

    for i in range(len(df)):
        if df['2列目ウォークスルー'][i] == '可':
            df['2列目ウォークスルー'][i] = 1
        else:
            df['2列目ウォークスルー'][i] = 0

    for i in range(len(df)):
        if df['3列目シート'][i] == '分割可倒':
            df['3列目シート'][i] = 1
        else:
            df['3列目シート'][i] = 0

    df.to_csv('./data/car_csv/car_data.csv',index=False)