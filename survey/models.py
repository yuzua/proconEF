from django.db import models

# Create your models here.
class AnswerModel(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    answer = models.CharField(max_length=999, verbose_name='結果')
    count = models.IntegerField(default=1, verbose_name='回数')

    def __str__(self):
        return '<answer_id=' + str(self.id) + '>'