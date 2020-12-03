from django.shortcuts import render
from django.http import HttpResponse
from django .shortcuts import redirect
from django.views.generic import TemplateView
import random
#from .forms import QuestionnaireAnswerForm

# Create your views here.
def index(request):
    return HttpResponse('survey')

class Survey(TemplateView):

    def __init__(self):
        survey_list = [
            '乗り心地',
            '荷室の使いやすさ',
            '燃費の良さ',
            '排気量の少なさ',
            '車内空間が広い',
            '静かに走る',
            '馬力がある',
            '乗車定員が多い',
            '小回りが利く',
            '乗車しやすい',
            '安全性能が高い',
            '走行性能が高い',
            '車両サイズが小さい',
            'カスタムしやすい',
            'オプションが充実してる',
        ]
        rsl = random.sample(survey_list, 5)
        print(rsl)
        self.params = {
            'title': 'アンケート',
            'message': '車選びで重視するものを選択してください',
            'data': rsl
        }

    def get(self, request):
        return render(request, 'survey/questionnaire.html', self.params)

    def post(self, request):
        checks_value = request.POST.getlist('checks[]')
        print(checks_value)
        for item in checks_value:
            if item == '乗り心地':
                print('1')
            elif item == '荷室の使いやすさ':
                print('2')
            elif item == '燃費の良さ':
                print('3')
            elif item == '排気量の少なさ':
                print('4')
            elif item == '車内空間が広い':
                print('5')
            elif item == '静かに走る':
                print('6')
            elif item == '馬力がある':
                print('7')
            elif item == '乗車定員が多い':
                print('8')
            elif item == '小回りが利く':
                print('9')
            elif item == '乗車しやすい':
                print('10')
            elif item == '安全性能が高い':
                print('11')
            elif item == '走行性能が高い':
                print('12')
            elif item == '車両サイズが小さい':
                print('13')
            elif item == 'カスタムしやすい':
                print('14')
            elif item == 'オプションが充実してる':
                print('15')
        return render(request, 'survey/questionnaire.html', self.params)         