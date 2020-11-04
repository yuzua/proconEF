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


# def katakana_only(value):
#         if(re.match(r'^[ァ-ヶ]*$', value) == None):
#             raise ValidationError(
#                 '%(value)s をカタカナで入力してください',\
#                 params={'value': value},
#             )

class HostUserModel(models.Model):

    day = models.DateField() 
    pay = models.CharField(max_length=32) 
    bank_name = models.CharField(max_length=32)
    bank_code = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    QR_id = models.CharField(max_length=100)

    def __str__(self):
         return '<カーシェアオーナー:id=' + str(self.id) + ',' + '(' + str(self.bank_name) + ')>'

class CarInfoModel(models.Model):

    license_plate = models.CharField(max_length=12)    	
    ParentCategory = models.CharField(max_length=32)
    category = models.CharField(max_length=32)
    model_id = models.CharField(max_length=128)
    custom = models.CharField(max_length=128)	
    people = models.IntegerField(default=0)
    day = models.DateField()
    tire = models.CharField(max_length=128)
    used_years = models.IntegerField(default=0)
    vehicle_inspection_day = models.DateField()

    def __str__(self):
         return '<車情報:id=' + str(self.id) + ',' + '(' + str(self.people) + ')>'
    


        