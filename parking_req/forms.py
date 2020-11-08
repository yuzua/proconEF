from django import forms
from.models import ParkingUserModel

# class ParkingForm(forms.Form):

#     #carsharing_id = forms.IntegerField(label='カーシェアリングID')
#     #parking_id = forms.CharField(label='駐車場ID')
#     coordinate = forms.CharField(label='駐車場座標')
#     day = forms.DateField(label='登録日')
#     parking_type = forms.CharField(label='駐車場タイプ')
#     width = forms.IntegerField(label='横幅')
#     length = forms.IntegerField(label='奥行き')
#     height = forms.IntegerField(label='高さ')
#     car_id = forms.IntegerField(label='車両ID')

class ParkingForm(forms.ModelForm):

    parkingtype_list = [
        ('平面駐車場', '平面駐車場'),
        ('立体駐車場', '立体駐車場'),
    ]
    parking_type = forms.ChoiceField(choices=parkingtype_list, label='駐車場タイプ')

    class Meta:
        model = ParkingUserModel
        fields = ['coordinate','parking_type','width','length','height']
        widget = {
            'coordinate': forms.TextInput(attrs={'class': 'form-control'}),
            'day': forms.DateInput(attrs={'class': 'form-control'}),
            #'parking_type': forms.NumberInput(attrs={'class': 'form-control'}),
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'user_id': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'coordinate': '駐車場座標',
            'day': '登録日',
            #'parking_type': '駐車場タイプ',
            'width': '横幅(m)',
            'length': '奥行き(m)',
            'height': '高さ(m)',
            'user_id': 'ユーザID',
        }

