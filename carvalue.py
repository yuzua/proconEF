import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pylab as plt
import seaborn as sns
%matplotlib inline

# dataNormal = pd.read_csv('sample-T.csv')
# dataNormal
# dataNormal.iloc[:,0:2].to_csv("test.csv",index=False)

# data = pd.read_csv("test.csv")
# data
dataNormal = pd.read_csv('sample-T.csv')
x = dataNormal.iloc[:,0:1]
y = dataNormal.iloc[:,18:19]
datasample = pd.concat([x,y],axis=1).to_csv("test.csv",index=False)
# float型にしないとモデルを推定する際にエラーがでる
data = data.astype({"トヨタ/プリウス":float})
# datetime型にしてインデックスにする
# data.Maker = pd.to_datetime(data.Maker)
# data = data.astype({"Maker":datetime64})
data.Maker = pd.to_datetime(data.Maker)
data = data.set_index("Maker")

#  自己相関のグラフ
import statsmodels.api as sm
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(data["トヨタ/プリウス"], lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(data["トヨタ/プリウス"], lags=40, ax=ax2)

seasonal_decompose_res = sm.tsa.seasonal_decompose(data["トヨタ/プリウス"], freq=12)
seasonal_decompose_res.plot()

# トレンド項あり（１次まで）、定数項あり
ct = sm.tsa.stattools.adfuller(data["トヨタ/プリウス"], regression="ct")
# トレンド項なし、定数項あり
c = sm.tsa.stattools.adfuller(data["トヨタ/プリウス"], regression="c")
# トレンド項なし、定数項なし
nc = sm.tsa.stattools.adfuller(data["トヨタ/プリウス"], regression="nc")

print("ct:")
print(ct[1])
print("---------------------------------------------------------------------------------------------------------------")
print("c:")
print(c[1])
print("---------------------------------------------------------------------------------------------------------------")
print("nc:")
print(nc[1])
print("---------------------------------------------------------------------------------------------------------------")

diff = data["トヨタ/プリウス"].diff()
diff = diff.dropna()

# トレンド項あり（１次まで）、定数項あり
ct = sm.tsa.stattools.adfuller(diff, regression="ct")
# トレンド項なし、定数項あり
c = sm.tsa.stattools.adfuller(diff, regression="c")
# トレンド項なし、定数項なし
nc = sm.tsa.stattools.adfuller(diff, regression="nc")

print("ct:")
print(ct[1])
print("---------------------------------------------------------------------------------------------------------------")
print("c:")
print(c[1])
print("---------------------------------------------------------------------------------------------------------------")
print("nc:")
print(nc[1])
print("---------------------------------------------------------------------------------------------------------------")

plt.plot(diff)

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
                            train_data["トヨタ/プリウス"], order=(p,d,q), 
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
    SARIMA_1_1_0_101 = sm.tsa.SARIMAX(train_data["トヨタ/プリウス"], order=(jadge[i][1][0],jadge[i][1][1],jadge[i][1][2]), seasonal_order=(jadge[i][1][3],jadge[i][1][4],jadge[i][1][5],12),initialization = 'approximate_diffuse').fit()

# 自動学習実験コード
# Ljungbox検定
    a = []
    ljungbox_result = sm.stats.diagnostic.acorr_ljungbox(SARIMA_1_1_0_101.resid, lags=10)
    df_ljungbox_result = pd.DataFrame({"p-value":ljungbox_result[1]})
    a = df_ljungbox_result[df_ljungbox_result["p-value"] <  0.05]

    sampletest = np.array(a)

    if len(sampletest) == 0:
        # 予測
        pred = SARIMA_1_1_0_101.predict('2018-11-01', '2020-12-01')
        # 実データと予測結果の図示
        plt.plot(train_data["トヨタ/プリウス"], label="train")
        plt.plot(pred, "r", label="pred")
        plt.legend()

        # 予測
        ts_pred = SARIMA_1_1_0_101.predict('2018-01-01', '2020-12-01')

        # 実データと予測結果の図示
        plt.plot(train_data["トヨタ/プリウス"], label='original')
        plt.plot(ts_pred, label='predicted', color='red')
        plt.legend(loc='best')
        print(ts_pred)
        break
    else:
        pass
# # 予測
# pred = SARIMA_1_1_0_101.predict('2018-11-01', '2020-12-01')
# # 実データと予測結果の図示
# plt.plot(train_data["トヨタ/プリウス"], label="train")
# plt.plot(pred, "r", label="pred")
# plt.legend()

# # 予測
# ts_pred = SARIMA_1_1_0_101.predict('2018-01-01', '2020-12-01')

# # 実データと予測結果の図示
# plt.plot(train_data["トヨタ/プリウス"], label='original')
# plt.plot(ts_pred, label='predicted', color='red')
# plt.legend(loc='best')
# print(ts_pred)

