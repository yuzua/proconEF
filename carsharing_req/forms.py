from django import forms
from django.core.mail import EmailMessage
from .models import CarsharUserModel

class CarsharUserCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(CarsharUserCreateForm, self).__init__(*args, **kwd)
        self.fields["gender"].required = False
    class Meta:
        model = CarsharUserModel
        fields = ['id', 'name', 'gender', 'age', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control'}),
        }
        labels={
           'name': '名前',
           'gender': '性別',
           'age': '年齢',
           'birthday': '生年月日',
        }