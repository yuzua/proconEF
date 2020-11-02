import re
from django.db import models
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

class CarsharOwnersModel(models.Model):
    
    car_maker = models.CharField(max_length=100) #ChoiceField
    car_type = models.CharField(max_length=100) #ChoiceField
    car_possible = models.IntegerField(default=0)
    car_number = models.IntegerField(default=0, validators=[number_only])
    bank_name = models.CharField(max_length=100, validators=[katakana_only]) #ChoiceField
    bank_num = models.IntegerField(default=0, validators=[number_only])
    account_num = models.IntegerField(default=0, validators=[number_only])
    account_name = models.CharField(max_length=100) #カタカナで入力
    
    
    def __str__(self):
         return '<カーシェアオーナー:id=' + str(self.id) + ',' + str(self.car_possible) + \
             ',' + str(self.car_number) + ',' + str(self.bank_num) + ',' + str(self.account_num) + \
             '(' + str(self.account_name) + ')>'
        