import re
from django.db import models
from datetime import date
from django.core.validators import ValidationError, MinValueValidator, MaxValueValidator


# def number_only(value):
#         if(re.match(r'^[0-9]*$', value) == None):
#             raise ValidationError(
#                 '%(value)s を半角数字で入力してください',\
#                 params={'value': value},
#             )


def katakana_only(value):
        if(re.match(r'^[ァ-ヶ]*$', value) == None):
            raise ValidationError(
                '%(value)s をカタカナで入力してください',\
                params={'value': value},
            )

class HostUserModel(models.Model):

    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    day = models.DateField() 
    pay = models.CharField(max_length=32) 
    bank_name = models.CharField(max_length=32, validators=[katakana_only])
    bank_code = models.IntegerField()
    bank_account_number = models.IntegerField()
    QR_id = models.IntegerField()

    def __str__(self):
         return '<カーシェアオーナー:id=' + str(self.user_id) + ',' + '(' + str(self.bank_name) + ')>'


class ParentCategory(models.Model):
    name = models.CharField('メーカー', max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('車種', max_length=255)
    parent = models.ForeignKey(ParentCategory, verbose_name='親カテゴリ', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Post(models.Model):
    parent_category = models.ForeignKey(ParentCategory, verbose_name='親カテゴリ', on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name='車種', default=0, on_delete=models.PROTECT)
    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    license_plate = models.CharField(max_length=12, verbose_name='ナンバープレート')    	
    model_id = models.CharField(max_length=128,  verbose_name='型番')
    custom = models.CharField(max_length=128,  verbose_name='カスタム')	
    people = models.IntegerField(default=0,  verbose_name='乗車人数')
    day = models.DateField(verbose_name='登録日')
    tire = models.CharField(max_length=128,  verbose_name='タイヤ')
    used_years = models.IntegerField(default=0,  verbose_name='使用年数(年単位)')
    vehicle_inspection_day = models.DateField( verbose_name='次回車検予定日')

    def __str__(self):
         return str(self.user_id) 


    
    


        