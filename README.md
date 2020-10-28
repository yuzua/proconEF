# proconEF

# info
__carsharing_req(カーシェアリング利用登録)__
1. models.pyにCarsharUserModel[class]を追加
2. forms.pyを作成し、models.pyで作ったmodelをimport
```bash
from.models import CarsharUserModel
```
3. forms.pyにCarsharUserModelを継承させたCarsharUserCreateForm[class]を記入
```bash
class CarsharUserCreateForm(forms.ModelForm):
    class Meta:
        model = CarsharUserModel
        fields = ['id', 'name', 'mail', ... ]
```

2. views.pyにTemplateViewをimport
```bash
from django.views.generic import TemplateView
```
3. views.pyにCarsharUser[class]を宣言(TemplateViewを使用)
4. views.pyのCarsharUser[class]にコンストラクタを設定
```bash
def __init__(self):
        self.params = {
            'title': 'タイトル',
        }
```
params内に使用変数を定義

4. urls.pyにviews.py内で宣言したCarsharUser[class]をimport
```bash
from .views import CarsharUser
```
5. urls.pyに以下の記述でアプリケーション名を追記
```bash
app_name = 'carsharing_req'
```
6. urls.pyにCarsharUserclassのディレクトリを追記
```bash
path('index/', CarsharUser.as_view(), name='index')
```

7. ルートディレクトリ直下のtemplatesフォルダ内にcarsharing_reqフォルダを作成
```bash
$ mkdir carsharing_req
```
8. carsharing_reqフォルダ内にindex.htmlを作成
```bash
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
    <title>{{ title }}</title>
</head>
<body class="container">
    <h1 class="display-4 text-primary">{{ title }}</h1>
    <p class="h5 mt-4">{{ message|safe }}</p>
    <form action="{% url 'index' %}" method="post">
        {% csrf_token %}
        {{ form.as_table }}
        <input class="btn btn-primary my-2" type="submit" value="click">
    </form>
</body>
</html>
```
9. さあ、runserverしてみよう

__carsharing_booking(カーシェア予約)__

__owners_req(カーシェアオーナー申請)__

__parking_req(駐車場オーナー申請)__

__secondhandcar(中古車提案)__

# Djangoでの開発の流れ 
## 11/4からの開発の時一回のみやって欲しいこと
①$pip install pipenv #Desktop上で
②仮想環境の設定へ

## 仮想環境の設定(開発の時毎回やってください)
$cd proconEF
$pipenv install #仮想環境の作成
$pipenv shell #仮想環境に入る(VSCodeのshellが$pipenv or Python~に変わっているか確認)

## Djangoコマンド
python manage.py makemigration #データベースにテーブル作成
python manage.oy migrate #データベースへ反映
python manage.py createrunserver #管理者アカウントの作成
python manage.py runserver #サーバー起動

# Gitコマンド&流れ
## 11/4からの開発時一回のみやって欲しいこと
①翔ちゃんのGithub(proconEF)をForkする
②$git clone <自分のGithubURL(proconEF)>　#URL先のフォルダを自分のPC上にコピー
③$git remote add remote <翔ちゃんのGithubURL(proconEF)> #URL先のフォルダを追加
③VSCodeの左下のmainを押してorigin/djangoをクリック
④11/4からの開発の時一回のみやって欲しいことへ

## 毎回開発の前にやって欲しいこと
①VSCodeの左下のmainを押してdjangoをクリック。
②$git pull remote django #前日の変更をローカルに適用
③仮想環境の設定へ

## 毎回開発後にやって欲しいこと
①$git add .
②$git commit -m "コメント入力"
③$git push origin django #①②③をやることで自分のGithub上のproconEFのdjangoブランチに変更が送られる
④Github上からpull requestsをクリック→翔ちゃんのproconEF djangoに自分のproconEF djangoからcreate pull requestを作成


