import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

#1個邪魔なデータあり(メルセデスＡＭＧ・/SLクラス)
sample = sample.drop(42, axis=0)

#データの読み込み(書き換え必要)
sample = pd.read_csv("sample-T.csv")

#前処理
sample = sample.drop(columns="メーカー ",axis=1)
sample = sample.drop(columns="車種 ",axis=1)
sample = sample.drop(columns="グレード ",axis=1)
sample = sample.drop(columns="発売期間",axis=1)
sample = sample.drop(columns="型式",axis=1)
sample = sample.drop(columns="最高出力/回転数(ps/rpm)",axis=1)
sample = sample.drop(columns="最大トルク/回転数(kg・m/rpm)",axis=1)
sample = sample.drop(columns="前タイヤ",axis=1)
sample = sample.drop(columns="後タイヤ",axis=1)
sample = sample.drop(columns="JC08モード燃費(km/L)",axis=1)
sample = sample.drop(columns="パワーウインドウ",axis=1)
sample = sample.drop(columns="運転席エアバッグ",axis=1)

#乗車定員
for i in range(len(sample)):
  if sample.at[i,"乗車定員"] == "2人":
    sample.at[i,"乗車定員"] = 2
  if sample.at[i,"乗車定員"] == "4人":
    sample.at[i,"乗車定員"] = 4
  if sample.at[i,"乗車定員"] == "5人":
    sample.at[i,"乗車定員"] = 5
  if sample.at[i,"乗車定員"] == "6人":
    sample.at[i,"乗車定員"] = 6
  if sample.at[i,"乗車定員"] == "7人":
    sample.at[i,"乗車定員"] = 7
  if sample.at[i,"乗車定員"] == "8人":
    sample.at[i,"乗車定員"] = 8

#駆動方式(one-hotエンコーディング)
sample = pd.get_dummies(sample,columns=["駆動方式"])

#ドア枚数
for i in range(len(sample)):
  if sample.at[i,"ドア枚数"] == "2ドア":
    sample.at[i,"ドア枚数"] = 2
  if sample.at[i,"ドア枚数"] == "3ドア":
    sample.at[i,"ドア枚数"] = 3
  if sample.at[i,"ドア枚数"] == "4ドア":
    sample.at[i,"ドア枚数"] = 4
  if sample.at[i,"ドア枚数"] == "5ドア":
    sample.at[i,"ドア枚数"] = 5

#エンジン型式
mode = sample.mode()
mode_change = mode.iloc[0][2]
sample["エンジン型式"] = sample["エンジン型式"].fillna(mode_change)
sample = pd.get_dummies(sample,columns=["エンジン型式"])

#エンジン種類
sample = pd.get_dummies(sample,columns=["エンジン種類"])

#エンジン区分
sample = pd.get_dummies(sample,columns=["エンジン区分"])

#環境対策エンジン
sample["環境対策エンジン"] = sample["環境対策エンジン"].fillna(0)
for i in range(len(sample)):
  if sample.iloc[i]["環境対策エンジン"] == 0:
    pass
  else:
    sample.at[i,"環境対策エンジン"] = 1

#総排気量
for i in range(len(sample)):
 replace = sample.iloc[i]["総排気量(cc)"].replace("cc","")
 sample.at[i,"総排気量(cc)"] = replace

#過給器
sample["過給器"] = sample["過給器"].fillna(0)
for i in range(len(sample)):
  if sample.iloc[i]["過給器"] == 0:
    pass
  else:
    sample.at[i,"過給器"] = 1

#ホイールベース
for i in range(len(sample)):
 replace = sample.iloc[i]["ホイールベース(mm)"].replace("mm","")
 sample.at[i,"ホイールベース(mm)"] = replace

#車両重量(kg)
for i in range(len(sample)):
 replace = sample.iloc[i]["車両重量(kg)"].replace("kg","")
 sample.at[i,"車両重量(kg)"] = replace

#最低地上高(mm)(中央値で補間)
sample["最低地上高(mm)"] = sample["最低地上高(mm)"].fillna("150mm")
for i in range(len(sample)): 
 replace = sample.iloc[i]["最低地上高(mm)"].replace("mm","")
 sample.at[i,"最低地上高(mm)"] = replace

#最小回転半径(m)(中央値で補間)
sample["最小回転半径(m)"] = sample["最小回転半径(m)"].fillna("5.2m")
for i in range(len(sample)): 
 replace = sample.iloc[i]["最小回転半径(m)"].replace("m","")
 sample.at[i,"最小回転半径(m)"] = replace

#サスペンション形式前
sample = pd.get_dummies(sample,columns=["サスペンション形式前"])

#サスペンション形式後
sample = pd.get_dummies(sample,columns=["サスペンション形式後"])

#ブレーキ形式前
sample = pd.get_dummies(sample,columns=["ブレーキ形式前"])

#ブレーキ形式後
sample = pd.get_dummies(sample,columns=["ブレーキ形式後"])

#使用燃料
sample = pd.get_dummies(sample,columns=["使用燃料"])

#燃料タンク容量(L)
for i in range(len(sample)): 
 replace = sample.iloc[i]["燃料タンク容量(L)"].replace("L","")
 sample.at[i,"燃料タンク容量(L)"] = replace

#オートエアコン
for i in range(len(sample)):
  if sample.iloc[i]["オートエアコン"] == "○":
    sample.at[i,"オートエアコン"] = 1
  else:
    sample.at[i,"オートエアコン"] = 0

#エアフイルター
for i in range(len(sample)):
  if sample.iloc[i]["エアフィルター"] == "○":
    sample.at[i,"エアフィルター"] = 1
  else:
    sample.at[i,"エアフィルター"] = 0

#シートリフター
for i in range(len(sample)):
  if sample.iloc[i]["シートリフター"] == "○":
    sample.at[i,"シートリフター"] = 1
  else:
    sample.at[i,"シートリフター"] = 0

#フロントベンチシート
for i in range(len(sample)):
  if sample.iloc[i]["フロントベンチシート"] == "○":
    sample.at[i,"フロントベンチシート"] = 1
  else:
    sample.at[i,"フロントベンチシート"] = 0

#2列目シート
for i in range(len(sample)):
  if sample.iloc[i]["2列目シート"] == "固定":
    sample.at[i,"2列目シート"] = 1
  else:
    sample.at[i,"2列目シート"] = 0

#UVカットガラス
for i in range(len(sample)):
  if sample.iloc[i]["UVカットガラス"] == "○":
    sample.at[i,"UVカットガラス"] = 1
  else:
    sample.at[i,"UVカットガラス"] = 0

#プライバシーガラス
for i in range(len(sample)):
  if sample.iloc[i]["プライバシーガラス"] == "○":
    sample.at[i,"プライバシーガラス"] = 1
  else:
    sample.at[i,"プライバシーガラス"] = 0

#アルミホイール
for i in range(len(sample)):
  if sample.iloc[i]["アルミホイール"] == "○":
    sample.at[i,"アルミホイール"] = 1
  else:
    sample.at[i,"アルミホイール"] = 0

#両側電動スライドドア
for i in range(len(sample)):
  if sample.iloc[i]["両側電動スライドドア"] == "○":
    sample.at[i,"両側電動スライドドア"] = 1
  else:
    sample.at[i,"両側電動スライドドア"] = 0

#リアスポイラー
for i in range(len(sample)):
  if sample.iloc[i]["リアスポイラー"] == "○":
    sample.at[i,"リアスポイラー"] = 1
  else:
    sample.at[i,"リアスポイラー"] = 0

#フロントフォグランプ
for i in range(len(sample)):
  if sample.iloc[i]["フロントフォグランプ"] == "○":
    sample.at[i,"フロントフォグランプ"] = 1
  else:
    sample.at[i,"フロントフォグランプ"] = 0

#スピーカ数
sample["スピーカ数"] = sample["スピーカ数"].fillna("zero")
for i in range(len(sample)):
  if sample.iloc[i]["スピーカ数"] == "zero":
    sample.at[i,"スピーカ数"] = 0
  else:
    sample.at[i,"スピーカ数"] = 1

#ETC
for i in range(len(sample)):
  if sample.iloc[i]["ETC"] == "○":
    sample.at[i,"ETC"] = 1
  else:
    sample.at[i,"ETC"] = 0


#助手席エアバッグ
for i in range(len(sample)):
  if sample.iloc[i]["助手席エアバッグ"] == "○":
    sample.at[i,"助手席エアバッグ"] = 1
  else:
    sample.at[i,"助手席エアバッグ"] = 0

#サイドエアバッグ
for i in range(len(sample)):
  if sample.iloc[i]["サイドエアバッグ"] == "○":
    sample.at[i,"サイドエアバッグ"] = 1
  else:
    sample.at[i,"サイドエアバッグ"] = 0

#カーテンエアバッグ
for i in range(len(sample)):
  if sample.iloc[i]["カーテンエアバッグ"] == "○":
    sample.at[i,"カーテンエアバッグ"] = 1
  else:
    sample.at[i,"カーテンエアバッグ"] = 0

#頸部衝撃緩和ヘッドレスト
for i in range(len(sample)):
  if sample.iloc[i]["頸部衝撃緩和ヘッドレスト"] == "○":
    sample.at[i,"頸部衝撃緩和ヘッドレスト"] = 1
  else:
    sample.at[i,"頸部衝撃緩和ヘッドレスト"] = 0

#EBD付ABS
for i in range(len(sample)):
  if sample.iloc[i]["EBD付ABS"] == "○":
    sample.at[i,"EBD付ABS"] = 1
  else:
    sample.at[i,"EBD付ABS"] = 0

#クルーズコントロール
for i in range(len(sample)):
  if sample.iloc[i]["クルーズコントロール"] == "○":
    sample.at[i,"クルーズコントロール"] = 1
  else:
    sample.at[i,"クルーズコントロール"] = 0

#ESC（横滑り防止装置）
for i in range(len(sample)):
  if sample.iloc[i]["ESC（横滑り防止装置）"] == "○":
    sample.at[i,"ESC（横滑り防止装置）"] = 1
  else:
    sample.at[i,"ESC（横滑り防止装置）"] = 0

#トラクションコントロール
for i in range(len(sample)):
  if sample.iloc[i]["トラクションコントロール"] == "○":
    sample.at[i,"トラクションコントロール"] = 1
  else:
    sample.at[i,"トラクションコントロール"] = 0

#ISOFIX対応チャイルドシート固定バー
for i in range(len(sample)):
  if sample.iloc[i]["ISOFIX対応チャイルドシート固定バー"] == "○":
    sample.at[i,"ISOFIX対応チャイルドシート固定バー"] = 1
  else:
    sample.at[i,"ISOFIX対応チャイルドシート固定バー"] = 0

#パワーステアリング
for i in range(len(sample)):
  if sample.iloc[i]["パワーステアリング"] == "○":
    sample.at[i,"パワーステアリング"] = 1
  else:
    sample.at[i,"パワーステアリング"] = 0

#盗難防止装置
for i in range(len(sample)):
  if sample.iloc[i]["盗難防止装置"] == "○":
    sample.at[i,"盗難防止装置"] = 1
  else:
    sample.at[i,"盗難防止装置"] = 0

#セキュリティアラーム
for i in range(len(sample)):
  if sample.iloc[i]["セキュリティアラーム"] == "○":
    sample.at[i,"セキュリティアラーム"] = 1
  else:
    sample.at[i,"セキュリティアラーム"] = 0

#キーレスエントリー
for i in range(len(sample)):
  if sample.iloc[i]["キーレスエントリー"] == "○":
    sample.at[i,"キーレスエントリー"] = 1
  else:
    sample.at[i,"キーレスエントリー"] = 0

#マニュアルモード
for i in range(len(sample)):
  if sample.iloc[i]["マニュアルモード"] == "○":
    sample.at[i,"マニュアルモード"] = 1
  else:
    sample.at[i,"マニュアルモード"] = 0

#チップアップシート
for i in range(len(sample)):
  if sample.iloc[i]["チップアップシート"] == "○":
    sample.at[i,"チップアップシート"] = 1
  else:
    sample.at[i,"チップアップシート"] = 0

#ドアイージークローザー
for i in range(len(sample)):
  if sample.iloc[i]["ドアイージークローザー"] == "○":
    sample.at[i,"ドアイージークローザー"] = 1
  else:
    sample.at[i,"ドアイージークローザー"] = 0

#アイドリングストップシステム
for i in range(len(sample)):
  if sample.iloc[i]["アイドリングストップシステム"] == "○":
    sample.at[i,"アイドリングストップシステム"] = 1
  else:
    sample.at[i,"アイドリングストップシステム"] = 0

#衝突軽減装置
for i in range(len(sample)):
  if sample.iloc[i]["衝突軽減装置"] == "○":
    sample.at[i,"衝突軽減装置"] = 1
  else:
    sample.at[i,"衝突軽減装置"] = 0

#レーンアシスト
for i in range(len(sample)):
  if sample.iloc[i]["レーンアシスト"] == "○":
    sample.at[i,"レーンアシスト"] = 1
  else:
    sample.at[i,"レーンアシスト"] = 0

#車間距離自動制御システム
for i in range(len(sample)):
  if sample.iloc[i]["車間距離自動制御システム"] == "○":
    sample.at[i,"車間距離自動制御システム"] = 1
  else:
    sample.at[i,"車間距離自動制御システム"] = 0

#バックモニター
for i in range(len(sample)):
  if sample.iloc[i]["バックモニター"] == "○":
    sample.at[i,"バックモニター"] = 1
  else:
    sample.at[i,"バックモニター"] = 0

#エンジンスタートボタン
for i in range(len(sample)):
  if sample.iloc[i]["エンジンスタートボタン"] == "○":
    sample.at[i,"エンジンスタートボタン"] = 1
  else:
    sample.at[i,"エンジンスタートボタン"] = 0

#前席シートヒーター
for i in range(len(sample)):
  if sample.iloc[i]["前席シートヒーター"] == "○":
    sample.at[i,"前席シートヒーター"] = 1
  else:
    sample.at[i,"前席シートヒーター"] = 0

#床下ラゲージボックス
for i in range(len(sample)):
  if sample.iloc[i]["床下ラゲージボックス"] == "○":
    sample.at[i,"床下ラゲージボックス"] = 1
  else:
    sample.at[i,"床下ラゲージボックス"] = 0

#オーディオソース_CD
for i in range(len(sample)):
  if sample.iloc[i]["オーディオソース_CD"] == "○":
    sample.at[i,"オーディオソース_CD"] = 1
  else:
    sample.at[i,"オーディオソース_CD"] = 0
  
#オーディオソース_DVD
for i in range(len(sample)):
  if sample.iloc[i]["オーディオソース_DVD"] == "○":
    sample.at[i,"オーディオソース_DVD"] = 1
  else:
    sample.at[i,"オーディオソース_DVD"] = 0

#オーディオソース_AM/FMラジオ
for i in range(len(sample)):
  if sample.iloc[i]["オーディオソース_AM/FMラジオ"] == "○":
    sample.at[i,"オーディオソース_AM/FMラジオ"] = 1
  else:
    sample.at[i,"オーディオソース_AM/FMラジオ"] = 0

#ブレーキアシスト
for i in range(len(sample)):
  if sample.iloc[i]["ブレーキアシスト"] == "○":
    sample.at[i,"ブレーキアシスト"] = 1
  else:
    sample.at[i,"ブレーキアシスト"] = 0

#駐車支援システム
for i in range(len(sample)):
  if sample.iloc[i]["駐車支援システム"] == "○":
    sample.at[i,"駐車支援システム"] = 1
  else:
    sample.at[i,"駐車支援システム"] = 0

#防水加工
for i in range(len(sample)):
  if sample.iloc[i]["防水加工"] == "○":
    sample.at[i,"防水加工"] = 1
  else:
    sample.at[i,"防水加工"] = 0

#地上波デジタルテレビチューナー
for i in range(len(sample)):
  if sample.iloc[i]["地上波デジタルテレビチューナー"] == "○":
    sample.at[i,"地上波デジタルテレビチューナー"] = 1
  else:
    sample.at[i,"地上波デジタルテレビチューナー"] = 0

#ソナー
for i in range(len(sample)):
  if sample.iloc[i]["ソナー"] == "○":
    sample.at[i,"ソナー"] = 1
  else:
    sample.at[i,"ソナー"] = 0

#フロントモニター
for i in range(len(sample)):
  if sample.iloc[i]["フロントモニター"] == "○":
    sample.at[i,"フロントモニター"] = 1
  else:
    sample.at[i,"フロントモニター"] = 0

#サイドモニター
for i in range(len(sample)):
  if sample.iloc[i]["サイドモニター"] == "○":
    sample.at[i,"サイドモニター"] = 1
  else:
    sample.at[i,"サイドモニター"] = 0

#ダウンヒルアシストコントロール
for i in range(len(sample)):
  if sample.iloc[i]["ダウンヒルアシストコントロール"] == "○":
    sample.at[i,"ダウンヒルアシストコントロール"] = 1
  else:
    sample.at[i,"ダウンヒルアシストコントロール"] = 0

#その他ナビゲーション
for i in range(len(sample)):
  if sample.iloc[i]["その他ナビゲーション"] == "○":
    sample.at[i,"その他ナビゲーション"] = 1
  else:
    sample.at[i,"その他ナビゲーション"] = 0

#寒冷地仕様
for i in range(len(sample)):
  if sample.iloc[i]["寒冷地仕様"] == "○":
    sample.at[i,"寒冷地仕様"] = 1
  else:
    sample.at[i,"寒冷地仕様"] = 0

#インテリジェントAFS
for i in range(len(sample)):
  if sample.iloc[i]["インテリジェントAFS"] == "○":
    sample.at[i,"インテリジェントAFS"] = 1
  else:
    sample.at[i,"インテリジェントAFS"] = 0

#運転席パワーシート
for i in range(len(sample)):
  if sample.iloc[i]["運転席パワーシート"] == "○":
    sample.at[i,"運転席パワーシート"] = 1
  else:
    sample.at[i,"運転席パワーシート"] = 0

#本革シート
for i in range(len(sample)):
  if sample.iloc[i]["本革シート"] == "○":
    sample.at[i,"本革シート"] = 1
  else:
    sample.at[i,"本革シート"] = 0

#AC電源
for i in range(len(sample)):
  if sample.iloc[i]["AC電源"] == "○":
    sample.at[i,"AC電源"] = 1
  else:
    sample.at[i,"AC電源"] = 0

#ステアリングヒーター
for i in range(len(sample)):
  if sample.iloc[i]["ステアリングヒーター"] == "○":
    sample.at[i,"ステアリングヒーター"] = 1
  else:
    sample.at[i,"ステアリングヒーター"] = 0

#リアフォグランプ
for i in range(len(sample)):
  if sample.iloc[i]["リアフォグランプ"] == "○":
    sample.at[i,"リアフォグランプ"] = 1
  else:
    sample.at[i,"リアフォグランプ"] = 0

#テレマティクスサービス
for i in range(len(sample)):
  if sample.iloc[i]["テレマティクスサービス"] == "○":
    sample.at[i,"テレマティクスサービス"] = 1
  else:
    sample.at[i,"テレマティクスサービス"] = 0

#高級サウンドシステム
for i in range(len(sample)):
  if sample.iloc[i]["高級サウンドシステム"] == "○":
    sample.at[i,"高級サウンドシステム"] = 1
  else:
    sample.at[i,"高級サウンドシステム"] = 0
  
#レインセンサー
for i in range(len(sample)):
  if sample.iloc[i]["レインセンサー"] == "○":
    sample.at[i,"レインセンサー"] = 1
  else:
    sample.at[i,"レインセンサー"] = 0

#インテリジェントパーキングアシスト
for i in range(len(sample)):
  if sample.iloc[i]["インテリジェントパーキングアシスト"] == "○":
    sample.at[i,"インテリジェントパーキングアシスト"] = 1
  else:
    sample.at[i,"インテリジェントパーキングアシスト"] = 0

#エマージェンシーサービス
for i in range(len(sample)):
  if sample.iloc[i]["エマージェンシーサービス"] == "○":
    sample.at[i,"エマージェンシーサービス"] = 1
  else:
    sample.at[i,"エマージェンシーサービス"] = 0

#フロント両席パワーシート
for i in range(len(sample)):
  if sample.iloc[i]["フロント両席パワーシート"] == "○":
    sample.at[i,"フロント両席パワーシート"] = 1
  else:
    sample.at[i,"フロント両席パワーシート"] = 0

#サンルーフ
for i in range(len(sample)):
  if sample.iloc[i]["サンルーフ"] == "○":
    sample.at[i,"サンルーフ"] = 1
  else:
    sample.at[i,"サンルーフ"] = 0

#オーディオソース_HDD
for i in range(len(sample)):
  if sample.iloc[i]["オーディオソース_HDD"] == "○":
    sample.at[i,"オーディオソース_HDD"] = 1
  else:
    sample.at[i,"オーディオソース_HDD"] = 0

#ニーエアバッグ
for i in range(len(sample)):
  if sample.iloc[i]["ニーエアバッグ"] == "○":
    sample.at[i,"ニーエアバッグ"] = 1
  else:
    sample.at[i,"ニーエアバッグ"] = 0

#シートポジションメモリー機能
for i in range(len(sample)):
  if sample.iloc[i]["シートポジションメモリー機能"] == "○":
    sample.at[i,"シートポジションメモリー機能"] = 1
  else:
    sample.at[i,"シートポジションメモリー機能"] = 0

#ヘッドライトウォッシャー
for i in range(len(sample)):
  if sample.iloc[i]["ヘッドライトウォッシャー"] == "○":
    sample.at[i,"ヘッドライトウォッシャー"] = 1
  else:
    sample.at[i,"ヘッドライトウォッシャー"] = 0

#後退時連動式ドアミラー
for i in range(len(sample)):
  if sample.iloc[i]["後退時連動式ドアミラー"] == "○":
    sample.at[i,"後退時連動式ドアミラー"] = 1
  else:
    sample.at[i,"後退時連動式ドアミラー"] = 0

#VGS/VGRS
for i in range(len(sample)):
  if sample.iloc[i]["VGS/VGRS"] == "○":
    sample.at[i,"VGS/VGRS"] = 1
  else:
    sample.at[i,"VGS/VGRS"] = 0

#10-15モード燃費(km/L)
sample["10-15モード燃費(km/L)"] = sample["10-15モード燃費(km/L)"].fillna("0km/L")
for i in range(len(sample)):
 replace = sample.iloc[i]["10-15モード燃費(km/L)"].replace("km/L","")
 sample.at[i,"10-15モード燃費(km/L)"] = replace

 #フロントスポイラー
 for i in range(len(sample)):
  if sample.iloc[i]["フロントスポイラー"] == "○":
    sample.at[i,"フロントスポイラー"] = 1
  else:
    sample.at[i,"フロントスポイラー"] = 0

#ディスチャージヘッドライト
for i in range(len(sample)):
  if sample.iloc[i]["ディスチャージヘッドライト"] == "○":
    sample.at[i,"ディスチャージヘッドライト"] = 1
  else:
    sample.at[i,"ディスチャージヘッドライト"] = 0

#オーディオソース_カセット
for i in range(len(sample)):
  if sample.iloc[i]["オーディオソース_カセット"] == "○":
    sample.at[i,"オーディオソース_カセット"] = 1
  else:
    sample.at[i,"オーディオソース_カセット"] = 0

#ABS
for i in range(len(sample)):
  if sample.iloc[i]["ABS"] == "○":
    sample.at[i,"ABS"] = 1
  else:
    sample.at[i,"ABS"] = 0

#バケットシート
for i in range(len(sample)):
  if sample.iloc[i]["バケットシート"] == "○":
    sample.at[i,"バケットシート"] = 1
  else:
    sample.at[i,"バケットシート"] = 0

#高性能ブレーキ
for i in range(len(sample)):
  if sample.iloc[i]["高性能ブレーキ"] == "○":
    sample.at[i,"高性能ブレーキ"] = 1
  else:
    sample.at[i,"高性能ブレーキ"] = 0

#LSD
for i in range(len(sample)):
  if sample.iloc[i]["LSD"] == "○":
    sample.at[i,"LSD"] = 1
  else:
    sample.at[i,"LSD"] = 0

#4WS
for i in range(len(sample)):
  if sample.iloc[i]["4WS"] == "○":
    sample.at[i,"4WS"] = 1
  else:
    sample.at[i,"4WS"] = 0

#後席シートヒーター
for i in range(len(sample)):
  if sample.iloc[i]["後席シートヒーター"] == "○":
    sample.at[i,"後席シートヒーター"] = 1
  else:
    sample.at[i,"後席シートヒーター"] = 0

#2列目ウォークスルー
for i in range(len(sample)):
  if sample.iloc[i]["2列目ウォークスルー"] == "可":
    sample.at[i,"2列目ウォークスルー"] = 1
  else:
    sample.at[i,"2列目ウォークスルー"] = 0

#3列目シート
sample["3列目シート"] = sample["3列目シート"].fillna(0)
for i in range(len(sample)):
  if sample.iloc[i]["3列目シート"] == 0:
    sample.at[i,"3列目シート"] = 0
  else:
    sample.at[i,"3列目シート"] = 1

#オットマン機構
for i in range(len(sample)):
  if sample.iloc[i]["オットマン機構"] == "○":
    sample.at[i,"オットマン機構"] = 1
  else:
    sample.at[i,"オットマン機構"] = 0

#電動バックドア
for i in range(len(sample)):
  if sample.iloc[i]["電動バックドア"] == "○":
    sample.at[i,"電動バックドア"] = 1
  else:
    sample.at[i,"電動バックドア"] = 0

#リアエンターテイメントシステム
for i in range(len(sample)):
  if sample.iloc[i]["リアエンターテイメントシステム"] == "○":
    sample.at[i,"リアエンターテイメントシステム"] = 1
  else:
    sample.at[i,"リアエンターテイメントシステム"] = 0

#電気式4WD
for i in range(len(sample)):
  if sample.iloc[i]["電気式4WD"] == "○":
    sample.at[i,"電気式4WD"] = 1
  else:
    sample.at[i,"電気式4WD"] = 0

#AI-SHIFT
for i in range(len(sample)):
  if sample.iloc[i]["AI-SHIFT"] == "○":
    sample.at[i,"AI-SHIFT"] = 1
  else:
    sample.at[i,"AI-SHIFT"] = 0

#助手席ウォークスルー
for i in range(len(sample)):
  if sample.iloc[i]["助手席ウォークスルー"] == "可":
    sample.at[i,"助手席ウォークスルー"] = 1
  else:
    sample.at[i,"助手席ウォークスルー"] = 0

#大型ガラスルーフ
for i in range(len(sample)):
  if sample.iloc[i]["大型ガラスルーフ"] == "○":
    sample.at[i,"大型ガラスルーフ"] = 1
  else:
    sample.at[i,"大型ガラスルーフ"] = 0

#ルーフレール
for i in range(len(sample)):
  if sample.iloc[i]["ルーフレール"] == "○":
    sample.at[i,"ルーフレール"] = 1
  else:
    sample.at[i,"ルーフレール"] = 0

#HDDナビゲーション
for i in range(len(sample)):
  if sample.iloc[i]["HDDナビゲーション"] == "○":
    sample.at[i,"HDDナビゲーション"] = 1
  else:
    sample.at[i,"HDDナビゲーション"] = 0

#ランフラットタイヤ
for i in range(len(sample)):
  if sample.iloc[i]["ランフラットタイヤ"] == "○":
    sample.at[i,"ランフラットタイヤ"] = 1
  else:
    sample.at[i,"ランフラットタイヤ"] = 0

#可変気筒装置
for i in range(len(sample)):
  if sample.iloc[i]["可変気筒装置"] == "○":
    sample.at[i,"可変気筒装置"] = 1
  else:
    sample.at[i,"可変気筒装置"] = 0

#AYC(アクティブ・ヨー・コントロール)
for i in range(len(sample)):
  if sample.iloc[i]["AYC(アクティブ・ヨー・コントロール)"] == "○":
    sample.at[i,"AYC(アクティブ・ヨー・コントロール)"] = 1
  else:
    sample.at[i,"AYC(アクティブ・ヨー・コントロール)"] = 0

#全長
for i in range(len(sample)): 
 replace = sample.iloc[i]["全長"].replace("mm","")
 sample.at[i,"全長"] = replace

#全幅
for i in range(len(sample)): 
 replace = sample.iloc[i]["全幅"].replace("mm","")
 sample.at[i,"全幅"] = replace

#全高
for i in range(len(sample)): 
 replace = sample.iloc[i]["全高"].replace("mm","")
 sample.at[i,"全高"] = replace

#室内全長
sample = sample.drop(columns="室内全長",axis=1)

#室内全幅
sample = sample.drop(columns="室内全幅",axis=1)

#室内全高
sample = sample.drop(columns="室内全高",axis=1)

#img1
sample = sample.drop(columns="img1",axis=1)

#img2
sample = sample.drop(columns="img2",axis=1)

#img3
sample = sample.drop(columns="img3",axis=1)

#フルフラットシート
for i in range(len(sample)):
  if sample.iloc[i]["フルフラットシート"] == "可":
    sample.at[i,"フルフラットシート"] = 1
  else:
    sample.at[i,"フルフラットシート"] = 0

#マニュアルエアコン
for i in range(len(sample)):
  if sample.iloc[i]["マニュアルエアコン"] == "○":
    sample.at[i,"マニュアルエアコン"] = 1
  else:
    sample.at[i,"マニュアルエアコン"] = 0

#両側スライドドア
for i in range(len(sample)):
  if sample.iloc[i]["両側スライドドア"] == "○":
    sample.at[i,"両側スライドドア"] = 1
  else:
    sample.at[i,"両側スライドドア"] = 0

#抗菌仕様
for i in range(len(sample)):
  if sample.iloc[i]["抗菌仕様"] == "○":
    sample.at[i,"抗菌仕様"] = 1
  else:
    sample.at[i,"抗菌仕様"] = 0

#ローダウン
for i in range(len(sample)):
  if sample.iloc[i]["ローダウン"] == "○":
    sample.at[i,"ローダウン"] = 1
  else:
    sample.at[i,"ローダウン"] = 0

#ナイトビジョン
for i in range(len(sample)):
  if sample.iloc[i]["ナイトビジョン"] == "○":
    sample.at[i,"ナイトビジョン"] = 1
  else:
    sample.at[i,"ナイトビジョン"] = 0

#高性能サスペンション
for i in range(len(sample)):
  if sample.iloc[i]["高性能サスペンション"] == "○":
    sample.at[i,"高性能サスペンション"] = 1
  else:
    sample.at[i,"高性能サスペンション"] = 0

#片側スライドドア
for i in range(len(sample)):
  if sample.iloc[i]["片側スライドドア"] == "○":
    sample.at[i,"片側スライドドア"] = 1
  else:
    sample.at[i,"片側スライドドア"] = 0

#ソフトトップ
sample = sample.drop(columns="ソフトトップ",axis=1)

#メタルトップ
sample = sample.drop(columns="メタルトップ",axis=1)

#空気清浄機
for i in range(len(sample)):
  if sample.iloc[i]["空気清浄機"] == "○":
    sample.at[i,"空気清浄機"] = 1
  else:
    sample.at[i,"空気清浄機"] = 0

#エアサスペンション
for i in range(len(sample)):
  if sample.iloc[i]["エアサスペンション"] == "○":
    sample.at[i,"エアサスペンション"] = 1
  else:
    sample.at[i,"エアサスペンション"] = 0

#センターデフロック
for i in range(len(sample)):
  if sample.iloc[i]["センターデフロック"] == "○":
    sample.at[i,"センターデフロック"] = 1
  else:
    sample.at[i,"センターデフロック"] = 0

#ハードトップ
for i in range(len(sample)):
  if sample.iloc[i]["ハードトップ"] == "○":
    sample.at[i,"ハードトップ"] = 1
  else:
    sample.at[i,"ハードトップ"] = 0

#キャンバストップ
sample = sample.drop(columns="キャンバストップ",axis=1)


14,15,16,17,18,19,20,21,24,29,32,34,35,38,40,41,42,47,52,54,59,61
