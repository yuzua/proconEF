def RecommendAI(path):

    #必要なライブラリをimport
    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans
    from sklearn import preprocessing
    from sklearn.metrics import  pairwise_distances_argmin_min
    import matplotlib.pyplot as plt
    from scipy.spatial.distance import cdist
    import json
    import os
    #アンケートデータ読み込み
    result_path = '/Django/data/recommend/' + path
    print(result_path)
    json_open = open(result_path, 'r')
    json_load = json.load(json_open)

    #アンケートデータ読み込んだら削除
    os.remove(result_path)


    #中古車スクレイピング用データ(数値変換済み)
    data = pd.read_csv('/Django/data/car_csv/car_data.csv')

    #最終結果出力のための車を格納しておくリスト
    saishu = []

    #sample_data：重み付けする特徴量のデータを退避したDataFrame(スケーリングしない)
    #sample：重み付けするデータを除いたDataFrame(スケーリングする)
    #norigocochi_list：重要度が高い特徴量のlist
    #omomi_list：値の高いデータを選択するためのlist
    #q_list = question
    question = []
    for i in json_load:
        question.append(i)
    for x in question:
        dataframe = data
        dataframe = dataframe.drop(['carID'],axis=1)
        car_data = data['carID']
        car_data = pd.DataFrame(car_data)
        if x == '乗り心地がいい':
            sample_data = dataframe[['最低地上高(mm)','車両重量(kg)','総排気量(cc)','燃料タンク容量(L)','全高(mm)','全幅(mm)','全長(mm)','最小回転半径(m)','ホイールベース(mm)']]
            sample = dataframe.drop(['最低地上高(mm)','車両重量(kg)','総排気量(cc)','燃料タンク容量(L)','全高(mm)','全幅(mm)','全長(mm)','最小回転半径(m)','ホイールベース(mm)'],axis=1)
            norigocochi_list = ['総排気量(cc)','ホイールベース(mm)','車両重量(kg)','最低地上高(mm)','最小回転半径(m)','燃料タンク容量(L)','全長(mm)','全幅(mm)','全高(mm)']
            omomi_list = ['最低地上高(mm)','車両重量(kg)','全高(mm)','最小回転半径(m)','ホイールベース(mm)']
        elif x == '燃費の良さ':
            sample_data = dataframe[['エンジン区分_ハイブリッド','車両重量(kg)','燃料タンク容量(L)','最低地上高(mm)','全高(mm)','全幅(mm)','過給器','駆動方式_FF','総排気量(cc)','リアフォグランプ']]
            sample = dataframe.drop(['エンジン区分_ハイブリッド','車両重量(kg)','燃料タンク容量(L)','最低地上高(mm)','全高(mm)','全幅(mm)','過給器','駆動方式_FF','総排気量(cc)','リアフォグランプ'],axis=1)
            norigocochi_list = ['エンジン区分_ハイブリッド','車両重量(kg)','燃料タンク容量(L)','最低地上高(mm)','全高(mm)','全幅(mm)','過給器','駆動方式_FF','総排気量(cc)','リアフォグランプ']
            omomi_list = ['エンジン区分_ハイブリッド','最低地上高(mm)','駆動方式_FF']
        elif x == '排気量の少なさ':
            sample_data = dataframe[['車両重量(kg)','総排気量(cc)','全長(mm)','最小回転半径(m)','全幅(mm)','ホイールベース(mm)','燃料タンク容量(L)']]
            sample = dataframe.drop(['車両重量(kg)','総排気量(cc)','全長(mm)','最小回転半径(m)','全幅(mm)','ホイールベース(mm)','燃料タンク容量(L)'],axis=1)
            norigocochi_list = ['車両重量(kg)','総排気量(cc)','全長(mm)','最小回転半径(m)','全幅(mm)','ホイールベース(mm)','燃料タンク容量(L)']
            omomi_list = []
        elif x == '乗車定員が多い':
            sample_data = dataframe[['乗車定員']]
            sample = dataframe.drop(['乗車定員'],axis=1)
            norigocochi_list = ['乗車定員']
            omomi_list = ['乗車定員']
        elif x == '小回りが利く':
            sample_data = dataframe[['エンジン型式_M15A-FXE','ホイールベース(mm)','全長(mm)','最低地上高(mm)','全高(mm)']]
            sample = dataframe.drop(['エンジン型式_M15A-FXE','ホイールベース(mm)','全長(mm)','最低地上高(mm)','全高(mm)'],axis=1)
            norigocochi_list = ['エンジン型式_M15A-FXE','ホイールベース(mm)','全長(mm)','最低地上高(mm)','全高(mm)']
            omomi_list = ['エンジン型式_M15A-FXE','ホイールベース(mm)','全長(mm)','全高(mm)']
        elif x == '乗車しやすい':
            sample_data = dataframe[['最低地上高(mm)','全高(mm)','車両重量(kg)','最小回転半径(m)','ホイールベース(mm)']]
            sample = dataframe.drop(['最低地上高(mm)','全高(mm)','車両重量(kg)','最小回転半径(m)','ホイールベース(mm)'],axis=1)
            norigocochi_list = ['最低地上高(mm)','全高(mm)','車両重量(kg)','最小回転半径(m)','ホイールベース(mm)']
            omomi_list = []
        elif x == '安全性能が高い':
            sample_data = dataframe[['車両重量(kg)','全長(mm)','総排気量(cc)','燃料タンク容量(L)','ホイールベース(mm)','最小回転半径(m)','最低地上高(mm)','全幅(mm)','全高(mm)','エンジン種類_直列3気筒DOHC']]
            sample = dataframe.drop(['車両重量(kg)','全長(mm)','総排気量(cc)','燃料タンク容量(L)','ホイールベース(mm)','最小回転半径(m)','最低地上高(mm)','全幅(mm)','全高(mm)','エンジン種類_直列3気筒DOHC'],axis=1)
            norigocochi_list = ['ホイールベース(mm)','最小回転半径(m)','最低地上高(mm)','全高(mm)','エンジン種類_直列3気筒DOHC']
            omomi_list = []
        elif x == '走行性能が高い':
            sample_data = dataframe[['最低地上高(mm)','車両重量(kg)','ホイールベース(mm)','全高(mm)','エンジン型式_2AR-FXE']]
            sample = dataframe.drop(['最低地上高(mm)','車両重量(kg)','ホイールベース(mm)','全高(mm)','エンジン型式_2AR-FXE'],axis=1)
            norigocochi_list = ['車両重量(kg)','ホイールベース(mm)','エンジン型式_2AR-FXE']
            omomi_list = []
        elif x == '車両サイズが小さい':
            sample_data = dataframe[['全幅(mm)','全長(mm)']]
            sample = dataframe.drop(['全幅(mm)','全長(mm)'],axis=1)
            norigocochi_list = ['全幅(mm)','全長(mm)']
            omomi_list = []
        elif x == '静かに走る':
            sample_data = dataframe[['エンジン型式_2ZR-FXE','エンジン型式_8GR-FXS','全長(mm)','車両重量(kg)','ホイールベース(mm)']]
            sample = dataframe.drop(['エンジン型式_2ZR-FXE','エンジン型式_8GR-FXS','全長(mm)','車両重量(kg)','ホイールベース(mm)'],axis=1)
            norigocochi_list = ['エンジン型式_2ZR-FXE','エンジン型式_8GR-FXS','全長(mm)','車両重量(kg)','ホイールベース(mm)']
            omomi_list = []
        elif x == '馬力がある':
            sample_data = dataframe[['最高出力(ps)']]
            sample = dataframe.drop(['最高出力(ps)'],axis=1)
            norigocochi_list = ['最高出力(ps)']
            omomi_list = ['最高出力(ps)']
        elif x == '荷室の使いやすさ':
            sample_data = dataframe[['防水加工','エンジン型式_LEB','最高出力(ps)','全高(mm)','室内全幅(mm)']]
            sample = dataframe.drop(['防水加工','エンジン型式_LEB','最高出力(ps)','全高(mm)','室内全幅(mm)'],axis=1)
            norigocochi_list = ['防水加工','エンジン型式_LEB','最高出力(ps)','全高(mm)','室内全幅(mm)']
            omomi_list = ['防水加工','エンジン型式_LEB','全高(mm)']
        elif x == '車内空間が広い':
            sample_data = dataframe[['室内全長(mm)','室内全幅(mm)','室内全高(mm)']]
            sample = dataframe.drop(['室内全長(mm)','室内全幅(mm)','室内全高(mm)'],axis=1)
            norigocochi_list = ['室内全長(mm)','室内全幅(mm)','室内全高(mm)']
            omomi_list = ['室内全長(mm)','室内全幅(mm)','室内全高(mm)']

        # スケーリング
        mmscaler = preprocessing.MinMaxScaler() 
        mmscaler.fit(sample)           
        y = mmscaler.transform(sample) 
        y = pd.DataFrame(y)
        sample_data = pd.DataFrame(sample_data)
        #乗り心地に関係する特徴量を戻す
        y = pd.concat([y,sample_data],axis=1)
        #クラスタリング
        model = KMeans(n_clusters=8,random_state=0)
        cl = model.fit(y)
        #クラスラベルをdfに追加
        car_data['クラスNo.'] = cl.labels_

        # 車出力のための処理
        result_list = []
        idx = []
        num = 0

        for i in norigocochi_list:
            Y = []
            Y = pd.DataFrame(Y)
            X = dataframe[i]
            a = pd.DataFrame(X)
            cls = KMeans(n_clusters=2)
            result = cls.fit(a)
            Y[i] = dataframe[i]
            Y['クラスタID'] = result.labels_
            cluster = Y.groupby('クラスタID').mean()
            #大きいクラスタNO取得
            if norigocochi_list[num] in omomi_list:
                if cluster.iloc[0].values >= cluster.iloc[1].values:
                    z = Y.query('クラスタID == 0').index
                    for d in z:
                        idx.append(d)
                else:
                    z = Y.query('クラスタID == 1').index
                    for d in z:
                        idx.append(d)
            else:
                if cluster.iloc[0].values >= cluster.iloc[1].values:
                    z = Y.query('クラスタID == 1').index
                    for d in z:
                        idx.append(d)
                else:
                    z = Y.query('クラスタID == 0').index
                    for d in z:
                        idx.append(d)
            num += 1

        kekka = pd.DataFrame(idx)
        sample = kekka.value_counts().head(5)

        tes = []
        resu = []
        index = sample.index
        for i in index:
            tes.append(i)
        for x in range(len(car_data)):
            if car_data['carID'][x] in tes:
                resu.append(car_data['クラスNo.'][x])


        resu = pd.DataFrame(resu) 
        cls = resu.value_counts()
        max = cls.max()
        #minと一致する要素を持ってるindexを抽出

        for i in range(len(cls)):
            if cls.iloc[i] == max:
                ff = pd.DataFrame(cls)
                ls = ff[i:i+1]
                aa = ls.index.values
                bb = aa[0]
                clasta = bb[0]

        clusassign = model.predict(y)
        min_dist = np.min(cdist(y, model.cluster_centers_, 'euclidean'), axis=1)
        Y = pd.DataFrame(min_dist, index=y.index, columns=['Center_euclidean_dist'])
        Z = pd.DataFrame(clusassign, index=y.index, columns=['cluster_ID'])
        PAP = pd.concat([Y,Z], axis=1)
        tmp = PAP[PAP['cluster_ID'].isin([clasta])].sort_values('Center_euclidean_dist').head(10)
        norigokochi = tmp.index

        df = norigokochi
        car_list = []
        for xx in df:
            car_list.append(xx)
        saishu.append(car_list)
        

    #最終出力
    ss = []
    ss = pd.DataFrame(ss)

    #最終結果を縦に連結
    for i in range(len(saishu)):
        m = pd.DataFrame(saishu[i])
        ss = pd.concat([ss,m])

    #全ての車が一意(全てバラバラ)の場合
    if len(ss[0].unique()) == len(ss):
        nagasa = len(saishu)
        hh = pd.DataFrame(saishu)
        num = []
        if nagasa == 1:
            num.append(hh.iloc[0].head(6))
        elif nagasa == 2:
            num.append(hh.iloc[0].head(3))
            num.append(hh.iloc[1].head(3))
        elif nagasa == 3:
            num.append(hh.iloc[0].head(2))
            num.append(hh.iloc[1].head(2))
            num.append(hh.iloc[2].head(2))
        elif nagasa == 4:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(2))
            num.append(hh.iloc[3].head(2))
        elif nagasa == 5:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(2))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
        elif nagasa == 6:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(1))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
            num.append(hh.iloc[5].head(1))
        elif nagasa == 7:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(1))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
            num.append(hh.iloc[5].head(1))
            num.append(hh.iloc[6].head(1))
        elif nagasa == 8:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(1))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
            num.append(hh.iloc[5].head(1))
            num.append(hh.iloc[6].head(1))
            num.append(hh.iloc[7].head(1))
        elif nagasa == 9:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(1))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
            num.append(hh.iloc[5].head(1))
            num.append(hh.iloc[6].head(1))
            num.append(hh.iloc[7].head(1))
            num.append(hh.iloc[8].head(1))
        elif nagasa == 10:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(1))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
            num.append(hh.iloc[5].head(1))
            num.append(hh.iloc[6].head(1))
            num.append(hh.iloc[7].head(1))
            num.append(hh.iloc[8].head(1))
            num.append(hh.iloc[9].head(1))
        elif nagasa == 11:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(1))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
            num.append(hh.iloc[5].head(1))
            num.append(hh.iloc[6].head(1))
            num.append(hh.iloc[7].head(1))
            num.append(hh.iloc[8].head(1))
            num.append(hh.iloc[9].head(1))
            num.append(hh.iloc[10].head(1))
        elif nagasa == 12:
            num.append(hh.iloc[0].head(1))
            num.append(hh.iloc[1].head(1))
            num.append(hh.iloc[2].head(1))
            num.append(hh.iloc[3].head(1))
            num.append(hh.iloc[4].head(1))
            num.append(hh.iloc[5].head(1))
            num.append(hh.iloc[6].head(1))
            num.append(hh.iloc[7].head(1))
            num.append(hh.iloc[8].head(1))
            num.append(hh.iloc[9].head(1))
            num.append(hh.iloc[10].head(1))
            num.append(hh.iloc[11].head(1))
        
        tmp = []
        for i in num:
            for x in range(len(i)):
                tmp.append(i[x])

    #重複している場合、重複している上位6車を抽出
    else:
        tmp = ss[0].value_counts().head(6).index
    

    #結果をjsonに変換
    tmp = pd.DataFrame(tmp)
    print(path)
    recopath = '/Django/data/recommend/reco_' + path
    print(recopath)
    path = path.replace('.json', '')
    print(path)
    tmp.columns = [path]
    tmp.to_json(recopath)


