from django import forms
from.models import BookingInfoModel

class BookingInfoForm(forms.ModelForm):

    class Meta:
        model = BookingInfoModel
        fields = ['car_id','start_day','end_day','start_time', 'end_time', 'charge']
        widget = {
            'car_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_day': forms.DateInput(attrs={'class': 'form-control'}),
            'end_day': forms.DateInput(attrs={'class': 'form-control'}),
            'start_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'end_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'charge': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'car_id': '車ID',
            'start_day': '利用開始日',
            'end_day': '利用終了日',
            'start_time': '利用開始時刻',
            'end_time': '利用終了時刻',
            'charge': '利用料金',
        }