from django.db import models


class CarsharOwnersModel(models.Model):
    
    car_maker = models.CharField(max_length=100) #ChoiceField
    car_type = models.CharField(max_length=100) #ChoiceField
    car_possible = models.IntegerField(max_length=10)
    car_number = models.IntegerField(max_length=4)
    bank_name = models.CharField(max_length=100) #ChoiceField
    bank_num = models.IntegerField(max_length=10)
    account_num = models.IntegerField(max_length=7)
    account_name = models.CharField(max_length=100) #カタカナで入力
    
    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + str(self.possible) + \
            '(' + str(self.age) + ')>'