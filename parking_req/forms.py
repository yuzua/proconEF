from django import forms
from.models import ParkingUserModel

class ParkingForm(forms.ModelForm):

    parkingtype_list = [
        ('平面駐車場', '平面駐車場'),
        ('立体駐車場', '立体駐車場'),
    ]
    parking_type = forms.ChoiceField(choices=parkingtype_list, label='駐車場タイプ', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ParkingUserModel
        fields = ['parking_type','width','length','height']
        widgets = {
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'width': '横幅(m)',
            'length': '奥行き(m)',
            'height': '高さ(m)',
        }

