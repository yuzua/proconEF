import re
from django.db import models
from datetime import date
from django.core.validators import ValidationError, MinValueValidator, MaxValueValidator, RegexValidator
from parking_req .models import ParkingUserModel
from django.core.validators import FileExtensionValidator


def katakana_only(value):
        if(re.match(r'^[ァ-ヶ]*$', value) == None):
            raise ValidationError(
                '%(value)s をカタカナで入力してください',\
                params={'value': value},
            )

class HostUserModel(models.Model):

    #id = models.IntegerField(default=0, verbose_name='オーナーID')
    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    day = models.DateField(verbose_name='登録日')
    # pay = models.CharField(max_length=32, verbose_name='支払方法')
    bank_code = models.CharField(max_length=4, verbose_name='銀行コード', \
        validators=[RegexValidator(r'^[0-9]{4}$', '数字4桁で入力して下さい。')] )
    bank_name = models.CharField(max_length=32, verbose_name='銀行名')
    branch_code = models.CharField(max_length=5, verbose_name='支店コード', \
        validators=[RegexValidator(r'^([0-9]{3})|([0-9]{5})$', '数字3桁(ゆうちょ銀行は5桁)で入力して下さい。')] )
    branch_name = models.CharField(max_length=32, verbose_name='支店名')
    bank_account_number = models.CharField(max_length=8, verbose_name='口座番号', \
        validators=[RegexValidator(r'^([0-9]{7})|([0-9]{8})$', '数字7桁(ゆうちょ銀行は8桁)で入力して下さい。')] )
    # QR_id = models.CharField(max_length=128, verbose_name='口座番号')

    def __str__(self):
         return '<カーシェアオーナー:id' + str(self.id) + '>'  


class ParentCategory(models.Model):
    parent_category = models.CharField('メーカー', max_length=255)

    def __str__(self):
        return self.parent_category


class Category(models.Model):
    category = models.CharField('車種', max_length=255)
    parent_category = models.ForeignKey(ParentCategory, verbose_name='親カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.category


class CarInfoModel(models.Model):
    # car_id = models.AutoField(primary_key=True) #車両ID
    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    day = models.DateField(verbose_name='登録日')
    parent_category = models.ForeignKey(ParentCategory, verbose_name='親カテゴリ', on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name='車種', default=0, on_delete=models.PROTECT)
    license_plate_place = models.CharField(max_length=4, verbose_name='ナンバープレート-運輸支局')
    license_plate_type = models.CharField(max_length=3, verbose_name='ナンバープレート-車両種類', \
        validators=[RegexValidator(r'^([0-9]{3})|([0-9]{2}[A-Z]{1})|([0-9]{1}[A-Z]{2})$')] )
    license_plate_how = models.CharField(max_length=1, verbose_name='ナンバープレート-使用用途', \
        validators=[RegexValidator(r'^[\u3041-\u309F]$', 'ひらがな１文字で入力して下さい。')] )
    license_plate_num = models.CharField(max_length=5, verbose_name='ナンバープレート-指定番号', \
        validators=[RegexValidator(r'^([0-9]{2})[-]([0-9]{2})$', 'ハイフンありの数字4文字で入力して下さい。\t\t例:\n01-23')] )
    model_id = models.CharField(max_length=128, verbose_name='型番')	
    people = models.IntegerField(default=0, verbose_name='乗車人数')
    tire = models.CharField(max_length=128, verbose_name='タイヤ')
    at_mt = models.CharField(max_length=2, verbose_name='AT or MT')
    babysheet = models.BooleanField(default=False, verbose_name='ベビーシート')
    car_nav = models.BooleanField(default=False, verbose_name='カーナビ')
    etc = models.BooleanField(default=False, verbose_name='ETC')
    car_autonomous = models.BooleanField(default=False, verbose_name='自動運転')
    around_view_monitor = models.BooleanField(default=False, verbose_name='アラウンドビューモニター')
    used_mileage = models.IntegerField(default=0, verbose_name='走行距離(km)')
    used_years = models.IntegerField(default=1, verbose_name='使用年数(年単位)', \
        validators=[RegexValidator(r'^([0-9]{1})|([0-9]{2})$'), MinValueValidator(1)] )
    vehicle_inspection_day = models.DateField(verbose_name='次回車検予定日')
    img = models.ImageField(
            upload_to='car/%Y/%m/%d/',
            #拡張子バリデーター。アップロードファイルの拡張子が違う時にエラー
            validators=[FileExtensionValidator(['jpg','png','gif', ])],
            blank=True, 
            null=True
        )
    key_flag =  models.BooleanField(default=False, verbose_name='鍵工事済み')

    def __str__(self):
         return '<car_id=' + str(self.id) + '>'


class CarInfoParkingModel(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    car_id = models.ForeignKey(CarInfoModel, on_delete=models.CASCADE, verbose_name='車両ID')
    parking_id =  models.ForeignKey(ParkingUserModel, on_delete=models.CASCADE, verbose_name='駐車場ID')
    def __str__(self):
        return '<user_id=' +str(self.user_id) + str(self.car_id) + str(self.parking_id) + '>'

class CarsharingDateModel(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    car_id = models.ForeignKey(CarInfoModel, on_delete=models.CASCADE, verbose_name='車両ID')
    possible_date = models.CharField(verbose_name='貸出可能日', max_length=10)

    def __str__(self):
      return '<date_id=' + str(self.user_id) + str(self.car_id) + self.possible_date + '>'