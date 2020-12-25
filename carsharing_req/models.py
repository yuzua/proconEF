from django.db import models
from carsharing_booking .models import BookingModel
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.validators import FileExtensionValidator

# Create your models here.

class CarsharUserModel(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_ja = models.CharField(max_length=100)
    last_ja = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    tel = models.CharField(max_length=15, \
        validators=[RegexValidator(r'^\d{10}$|^\d{11}$', 'ハイフン無しの数字で入力して下さい。')] )
    zip01 = models.IntegerField(max_length=7, \
        validators=[RegexValidator(r'^\d{7}$', 'ハイフン無しの数字で入力して下さい。')] )
    pref01 = models.CharField(max_length=100)
    addr01 = models.CharField(max_length=100)
    addr02 = models.CharField(max_length=100)
    system_flag = models.IntegerField(default=0)
    # img = models.FileField(
    img = models.ImageField(
        upload_to='users/license/%Y/%m/%d/',
        #拡張子バリデーター。アップロードファイルの拡張子が違う時にエラー
        validators=[FileExtensionValidator(['jpg','png','gif', ])],
        blank=True, 
        null=True
    )
    # カード情報
    credit_card_company = models.CharField(max_length=50)
    first_en = models.CharField(max_length=100, \
        validators=[RegexValidator(r'^[A-Z]*$', '半角英大文字で入力して下さい。')] )
    last_en = models.CharField(max_length=100, \
        validators=[RegexValidator(r'^[A-Z]*$', '半角英大文字で入力して下さい。')] )
    credit_card_num = models.CharField(max_length=300, \
        validators=[RegexValidator(r'^\d{16}$')] )
        # 本番用バリデーション
        # '^(4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12}|^(?:2131|1800|35\d{3})\d{11}$)$'
    credit_card_num_check = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(999)])
    valid_thru = models.CharField(max_length=5, \
        validators=[RegexValidator(r'^([0-9]{2})[/]([0-9]{2})$', '月/年\nの型式で入力して下さい。\t\t例:2025年3月の場合\n03/25')] )
    credit_card_num_check = models.IntegerField(validators=[MinValueValidator(000), MaxValueValidator(999)]) 
    security_code = models.CharField(max_length=300, \
        validators=[RegexValidator(r'^\d{3}$')] )
    # security_code = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(999)])
    plan = models.CharField(max_length=30)

    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.first_name + ' ' + self.last_name + '(' + str(self.age) + ')>'


class UsageModel(models.Model):
    
    user_id = models.IntegerField()
    car_id = models.IntegerField()
    booking_id = models.ForeignKey(BookingModel, verbose_name='予約番号', default=0, on_delete=models.PROTECT)
    start_day = models.CharField(verbose_name='開始日', max_length=10)
    start_time = models.CharField(verbose_name='開始時刻', max_length=5)
    end_day = models.CharField(verbose_name='終了日', max_length=10)
    end_time = models.CharField(verbose_name='終了時刻', max_length=5)
    charge = models.IntegerField(default=1000, verbose_name='利用料金')
    regist_date = models.DateTimeField(default=timezone.now, verbose_name='登録日時')

    def __str__(self):
        return '<carshar_usage_id=' + str(self.id) + '>'