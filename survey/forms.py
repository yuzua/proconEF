from django import forms
from.models import QuestionnaireDataModel, QuestionnaireAnswerModel

# class QuestionnaireAnswerForm(forms.Form):

#     class Meta:
#         model = QuestionnaireAnswerModel
#         # fields = ['answer_1','answer_2','answer_3','answer_4','answer_5',\
#         #     'answer_6','answer_7','answer_8','answer_9','answer_10',\
#         #         'answer_11','answer_12','answer_13','answer_14','answer_15',]
#         fields = ['answer_1','answer_2','answer_3']
#         widgets = {
#             'answer1': forms.CheckboxInput(attrs={'class': 'check'}),
#             'answer2': forms.CheckboxInput(attrs={'class': 'check'}),
#             'answer3': forms.CheckboxInput(attrs={'class': 'check'}),
#         }
#         labels = {
#             'answer1': '乗り心地',
#             'answer2': '荷室の使いやすさ',
#             'answer3': '燃費の良さ',
#         }

# class QuestionnaireAnswerForm(forms.Form):
#     answer1 = forms.BooleanField(label='乗り心地', required=False,)
#     answer2 = forms.BooleanField(label='荷室の使いやすさ', required=False)
#     answer3 = forms.BooleanField(label='燃費の良さ', required=False)        