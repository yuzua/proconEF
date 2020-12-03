from django.db import models

# Create your models here.
class QuestionnaireDataModel(models.Model):
    user_id = models.IntegerField(default=0, verbose_name='ユーザID')
    carshar_booking_id = models.IntegerField(default=0, verbose_name='予約ID')
    mileage = models.IntegerField(default=0, verbose_name='走行距離')
    destination = models.CharField(max_length=32, verbose_name='目的地')
    scene = models.CharField(max_length=32, verbose_name='シーン')

    def __str__(self):
        return '<questionnaire_id=' + str(self.id) + '>'

class QuestionnaireAnswerModel(models.Model):
    user_id = models.IntegerField(default=0, max_length=32, verbose_name='ユーザID')
    answer_1 = models.CharField(null=True, max_length=32, blank=True, verbose_name='乗り心地')
    answer_2 = models.CharField(null=True, max_length=32, blank=True, verbose_name='荷室の使いやすさ')
    answer_3 = models.CharField(null=True, max_length=32, blank=True,  verbose_name='燃費の良さ')
    answer_4 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='排気量の少なさ')
    answer_5 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='車内空間が広い')
    answer_6 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='静かに走る')
    answer_7 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='馬力がある')
    answer_8 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='乗車定員が多い')
    answer_9 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='小回りが利く')
    answer_10 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='乗り降りしやすい')
    answer_11 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='安全性能が高い')
    answer_12 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='走行性能が高い')
    answer_13 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='車両サイズが小さい')
    answer_14 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='カスタムしやすい')
    answer_15 = models.CharField(null=True, max_length=32,  blank=True, verbose_name='オプションが充実してる')

    def __str__(self):
        return '<questionnaire_answer_id=' + str(self.id) + '<user_id=' + str(self.user_id) + '>' + '>'
