from django import forms
from django.core.mail import EmailMessage
from .models import BookingModel

class BookingCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(BookingCreateForm, self).__init__(*args, **kwd)

    class Meta:
        model = BookingModel
        fields = ['start_day', 'start_time', 'end_day', 'end_time']
        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'car_id': forms.TextInput(attrs={'class': 'form-control'}),
            'start_day': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TextInput(attrs={'class': 'form-control'}),
            'end_day': forms.TextInput(attrs={'class': 'form-control'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels={
            'user_id': 'ユーザID',
            'car_id': '車両ID',
            'start_day': '開始日',
            'start_time': '開始時刻',
            'end_day': '終了日',
            'end_time': '終了時刻',
        }