from django.db import models
from carsharing_booking .models import BookingModel
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
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
    tel = models.CharField(max_length=15)
    zip01 = models.IntegerField(max_length=7)
    pref01 = models.CharField(max_length=100)
    addr01 = models.CharField(max_length=100)
    addr02 = models.CharField(max_length=100)
    system_flag = models.IntegerField(default=0)
    img = models.FileField(
            upload_to='users/license/%Y/%m/%d/',
            #拡張子バリデーター。アップロードファイルの拡張子が違う時にエラー
            validators=[FileExtensionValidator(['jpg','png','gif', ])],
            blank=True, 
            null=True
        )
    # カード情報
    credit_card_company = models.CharField(max_length=50)
    first_en = models.CharField(max_length=100)
    last_en = models.CharField(max_length=100)
    credit_card_num = models.CharField(max_length=300)
    credit_card_num_check = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(999)])
    valid_thru = models.CharField(max_length=5)
    security_code = models.CharField(max_length=300)
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