from django.db import models


class CarsharOwnersModel(models.Model):
    
    car_maker = models.CharField(max_length=100) #ChoiceField
    car_type = models.CharField(max_length=100) #ChoiceField
    car_possible = models.IntegerField(default=0)
    car_number = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=100) #ChoiceField
    bank_num = models.IntegerField(default=0)
    account_num = models.IntegerField(default=0)
    account_name = models.CharField(max_length=100) #カタカナで入力
    
    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + str(self.car_possible) + \
            ',' + str(self.car_number) + ',' + str(self.bank_num) + ',' + str(self.account_num) + \
            '(' + str(self.account_name) + ')>'