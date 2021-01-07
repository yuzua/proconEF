from django import forms
from.models import ParkingUserModel
from parking_booking .models import ParkingBookingModel
import bootstrap_datepicker_plus as datetimepicker


class ParkingForm(forms.ModelForm):

    PARKINGTYPE_LIST = [
        ('平面駐車場', '平面駐車場'),
        ('立体駐車場', '立体駐車場'),
    ]
    parking_type = forms.ChoiceField(choices=PARKINGTYPE_LIST, label='駐車場タイプ', widget=forms.Select(attrs={'class': 'form-control'}))
    GROUNDTYPE_LIST = [
        ('コンクリート', 'コンクリート'),
        ('平地', '平地'),
        ('砂利', '砂利'),
        ('砂地', '砂地'),
    ]
    ground_type = forms.ChoiceField(choices=GROUNDTYPE_LIST, label='土地タイプ', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ParkingUserModel
        fields = ['parking_type', 'ground_type', 'width','length','height']
        widgets = {
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'readonly':''})
        }
        labels = {
            'width': '横幅(m)',
            'length': '奥行き(m)',
            'height': '高さ(m)',
        }



class ParkingLoaningForm(forms.ModelForm):
    def __init__(self, *args, **kwd):
        super(ParkingLoaningForm, self).__init__(*args, **kwd)

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
            'start_day': '貸し出し制限開始日',
            'end_day': '貸し出し制限終了日',
            'start_time': '貸し出し制限開始時刻',
            'end_time': '貸し出し制限終了時刻',
        }