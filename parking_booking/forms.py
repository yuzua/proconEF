from django import forms
from.models import ParkingBookingModel
import bootstrap_datepicker_plus as datetimepicker

class ParkingBookingForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(ParkingBookingForm, self).__init__(*args, **kwd)

    class Meta:
        model = ParkingBookingModel
        fields = ['start_day', 'start_time', 'end_day', 'end_time']
        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'parking_id': forms.TextInput(attrs={'class': 'form-control'}),
            'start_day': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).start_of('期間'),
            'start_time': datetimepicker.DateTimePickerInput(
                format='%H:%M',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            'end_day': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).end_of('期間'),
            'end_time': datetimepicker.DateTimePickerInput(
                format='%H:%M',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }
        labels = {
            'start_day': '利用開始日',
            'end_day': '利用終了日',
            'start_time': '利用開始時刻',
            'end_time': '利用終了時刻',
            'charge': '利用料金',
        }