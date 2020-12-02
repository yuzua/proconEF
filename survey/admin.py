from django.contrib import admin
from .models import QuestionnaireDataModel, QuestionnaireAnswerModel


# Register your models here.
admin.site.register(QuestionnaireDataModel)
admin.site.register(QuestionnaireAnswerModel)