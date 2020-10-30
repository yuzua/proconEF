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

class ParkingForm(forms.Form):
    class Meta:
        model = ParkingUserModel
        fields = ['駐車場座標', '登録日', '駐車場タイプ', '横幅', '奥行き', '高さ', '車両ID']