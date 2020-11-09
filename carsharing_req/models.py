from django.db import models

# Create your models here.

class CarsharUserModel(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    zip01 = models.IntegerField()
    pref01 = models.CharField(max_length=100)
    addr01 = models.CharField(max_length=100)
    addr02 = models.CharField(max_length=100)
    system_flag = models.IntegerField(default=0)

    
    def __str__(self):
        return '<Friend:id=' + str(self.id) + ',' + self.name + '(' + str(self.age) + ')>'