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

# Gitコマンド&流れ
## 11/4からの開発時一回のみやること
1. 翔ちゃんのGithub(proconEF)をForkする
2. $git clone <自分のGithubURL(proconEF)>　#URL先のフォルダを自分のPC上にコピー
3. $git remote add remote <翔ちゃんのGithubURL(proconEF)> #URL先のフォルダを追加
4. VSCodeの左下のmainを押してorigin/djangoをクリック
5. 11/4からの開発の時一回のみやって欲しいことへ

## 毎回開発の前にやること
1. VSCodeの左下のmainを押してdjangoをクリック
2. $git pull remote django #前日の変更をローカルに適用
3. 仮想環境の設定へ

## 毎回開発後にやること
1. $git add .
2. $git commit -m "コメント入力"
3. $git push origin django #①②③をやることで自分のGithub上のproconEFのdjangoブランチに変更が送られる
4. Github上からpull requestsをクリック→翔ちゃんのproconEF djangoに自分のproconEF djangoからcreate pull requestを作成

# Djangoでの開発の流れ 
## 11/4からの開発の時一回のみやること
1. $pip install pipenv #Desktop上で
2. 仮想環境の設定へ

## 仮想環境の設定(開発の時毎回やってください)
$cd proconEF<br>
$pipenv install #仮想環境の作成<br>
$pipenv shell #仮想環境に入る(VSCodeのshellが$pipenv or Python~に変わっているか確認)<br>

## Djangoコマンド
python manage.py makemigration #データベースにテーブル作成<br>
python manage.oy migrate #データベースへ反映<br>
python manage.py createrunserver #管理者アカウントの作成<br>
python manage.py runserver #サーバー起動<br>


