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
5. urls.pyにCarsharUserclassのディレクトリを追記
```bash
path('index/', CarsharUser.as_view(), name='index')
```
6. ルートディレクトリ直下のtemplatesフォルダ内にcarsharing_reqフォルダを作成
```bash
$ mkdir carsharing_req
```
7. carsharing_reqフォルダ内にindex.htmlを作成
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
8. さあ、runserverしてみよう

__carsharing_booking(カーシェア予約)__
__owners_req(カーシェアオーナー申請)__
__parking_req(駐車場オーナー申請)__
__secondhandcar(中古車提案)__

# — Djangoのあれこれ —
#サーバーを立ち上げる
```bash
python manage.py runserver
```

#マイグレーションファイルの作成
```bash
python manage.py makemigrations
```


#データベースへ反映
```bash
python manage.py migrate
```


#管理者アカウントの作成
```bash
python manage.py createsuperuser
```


