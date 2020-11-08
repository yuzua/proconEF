import re
from django.db import models
from datetime import date
from django.core.validators import ValidationError

def number_only(value):
        if(re.match(r'^[0-9]*$', value) == None):
            raise ValidationError(
                '%(value)s を半角数字で入力してください',\
                params={'value': value},
            )


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
    bank_code = models.CharField(max_length=64, validators=[number_only])
    bank_account_number = models.CharField(max_length=64, validators=[number_only])
    QR_id = models.CharField(max_length=100, validators=[number_only])

    def __str__(self):
         return '<カーシェアオーナー:id=' + str(self.user_id) + ',' + '(' + str(self.bank_name) + ')>'

# class CarInfoModel(models.Model):

#     license_plate = models.CharField(max_length=12)    	
#     ParentCategory = models.CharField(max_length=32)
#     category = models.CharField(max_length=32)
#     model_id = models.CharField(max_length=128)
#     custom = models.CharField(max_length=128)	
#     people = models.IntegerField(default=0)
#     day = models.DateField()
#     tire = models.CharField(max_length=128)
#     used_years = models.IntegerField(default=0)
#     vehicle_inspection_day = models.DateField()
#     def __str__(self):
#          return '<車情報:id=' + str(self.id) + ',' + '(' + str(self.people) + ')>'

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
    

    category = models.ForeignKey(Category, verbose_name='カテゴリ', default=0, on_delete=models.PROTECT)
    license_plate = models.CharField(max_length=12,  verbose_name='ナンバープレート')    	
    #ParentCategory = models.CharField(max_length=32,  verbose_name='メーカー')
    model_id = models.CharField(max_length=128,  verbose_name='型番')
    custom = models.CharField(max_length=128,  verbose_name='カスタム')	
    people = models.IntegerField(default=0,  verbose_name='乗車人数')
    day = models.DateField( verbose_name='登録日')
    tire = models.CharField(max_length=128,  verbose_name='タイヤ')
    used_years = models.IntegerField(default=0,  verbose_name='使用年数')
    vehicle_inspection_day = models.DateField( verbose_name='次回車検予定日',)

    
    


        