def date():
    import datetime
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = dt_now.month

    if month <= 6:
        kako_year = year - 1
        if month == 1:
            kako_month = '07'
            mirai_month = '06'
        elif month == 2:
            kako_month = '08'
            mirai_month = '07'
        elif month == 3:
            kako_month = '09'
            mirai_month = '08'
        elif month == 4:
            kako_month = '10'
            mirai_month = '09'
        elif month == 5:
            kako_month ='11'
            mirai_month = '10'
        else:
            kako_motn = '12'
            mirai_month = '11'
        start = str(kako_year) + '-' + kako_month + '-' + '01'
        end = str(year) + '-' + mirai_month+ '-' + '01'

    elif month >= 8:
        mirai_year = year + 1
        if month == 8:
            kako_month = '02'
            mirai_month = '01'
        elif month == 9:
            kako_month = '03'
            mirai_month = '02'
        elif month == 10:
            kako_month = '04'
            mirai_month = '03'
        elif month == 11:
            kako_month = '05'
            mirai_month ='04'
        else:
            kako_month = '06'
            mirai_motn = '05'
        start = str(year) + '-' + kako_month + '-' + '01'
        end = str(mirai_year) + '-' + mirai_month+ '-' + '01'
    else:
        kako_month = '01'
        mirai_month = '12'
        start = str(year) + '-' + kako_month + '-' + '01'
        end = str(year) + '-' + mirai_month+ '-' + '01'

    return start,end


def kakakuyosoku():
    import numpy as np
    import pandas as pd
    from scipy import stats
    import datetime
    import os
    import statsmodels.api as sm

    df = pd.read_csv('car_value_data.csv')
    dataNormal = df.drop(['Maker'],axis=1)
    for shashu in dataNormal:
        #nanが含まれていればその列を削除する
        if dataNormal[shashu].isnull().any():
            pass
        else:            
            y = dataNormal[shashu]
            x = df['Maker']
            datasample = pd.concat([x,y],axis=1).to_csv("test.csv",index=False)

            data = pd.read_csv("test.csv")
            #読み込んだらファイルを削除
            os.remove("test.csv")
            data = data.astype({shashu:float})
            # datetime型にしてインデックスにする
            data.Maker = pd.to_datetime(data.Maker)
            data = data.set_index("Maker")

            # トレンド項あり（１次まで）、定数項あり
            ct = sm.tsa.stattools.adfuller(data[shashu], regression="ct")
            # トレンド項なし、定数項あり
            c = sm.tsa.stattools.adfuller(data[shashu], regression="c")
            # トレンド項なし、定数項なし
            nc = sm.tsa.stattools.adfuller(data[shashu], regression="nc")

            diff = data[shashu].diff()
            diff = diff.dropna()

            # トレンド項あり（１次まで）、定数項あり
            ct = sm.tsa.stattools.adfuller(diff, regression="ct")
            # トレンド項なし、定数項あり
            c = sm.tsa.stattools.adfuller(diff, regression="c")
            # トレンド項なし、定数項なし
            nc = sm.tsa.stattools.adfuller(diff, regression="nc")


            train_data = data[data.index < "2018-12"]
            # テストデータはテスト期間以前の日付も含まなければいけない
            test_data = data[data.index >= "2019-01"]



            # 総当たりで、AICが最小となるSARIMAの次数を探す
            max_p = 3
            max_q = 3
            max_d = 2
            max_sp = 1
            max_sq = 1
            max_sd = 1

            pattern = max_p*(max_d + 1)*(max_q + 1)*(max_sp + 1)*(max_sq + 1)*(max_sd + 1)

            modelSelection = pd.DataFrame(index=range(pattern), columns=["model", "aic"])

            # 自動SARIMA選択
            num = 0
            jadge = []

            for p in range(1, max_p + 1):
                for d in range(0, max_d + 1):
                    for q in range(0, max_q + 1):
                        for sp in range(0, max_sp + 1):
                            for sd in range(0, max_sd + 1):
                                for sq in range(0, max_sq + 1):
                                    sarima = sm.tsa.SARIMAX(
                                        train_data[shashu], order=(p,d,q), 
                                        seasonal_order=(sp,sd,sq,12), 
                                        enforce_stationarity = False, 
                                        enforce_invertibility = False
                                    ).fit()
                                    modelSelection.loc[num]["model"] = "order=(" + str(p) + ","+ str(d) + ","+ str(q) + "), season=("+ str(sp) + ","+ str(sd) + "," + str(sq) + ")"
                                    modelSelection.loc[num]["aic"] = sarima.aic
                                    jadge_x = []
                                    jadge_y = []
                                    jadge_z =[]
                                    jadge_x.append(sarima.aic)
                                    jadge_y.extend([p,d,q,sp,sd,sq])
                                    jadge_z.extend([jadge_x,jadge_y])
                                    jadge.append(jadge_z)
                                    num = num + 1

            modelSelection.sort_values(by='aic').head()
            jadge.sort()

            for i in range(len(jadge)):
                SARIMA_1_1_0_101 = sm.tsa.SARIMAX(train_data[shashu], order=(jadge[i][1][0],jadge[i][1][1],jadge[i][1][2]), seasonal_order=(jadge[i][1][3],jadge[i][1][4],jadge[i][1][5],12),initialization = 'approximate_diffuse').fit()

            # 自動学習実験コード
            # Ljungbox検定
                a = []
                ljungbox_result = sm.stats.diagnostic.acorr_ljungbox(SARIMA_1_1_0_101.resid, lags=10)
                df_ljungbox_result = pd.DataFrame({"p-value":ljungbox_result[1]})
                a = df_ljungbox_result[df_ljungbox_result["p-value"] <  0.05]

                sampletest = np.array(a)

                if len(sampletest) == 0:
                    # 今日の日付+-24週間
                    start,end = date()
                    # 予測
                    ts_pred = SARIMA_1_1_0_101.predict(start, end)

                    shashu = shashu.replace('/','|')
                    filename = shashu + '.csv'
                    ts_pred.to_csv(filename)
                    break
                else:
                    pass