from django import forms
from parking_req .models import ParkingUserModel

class AdminParkingForm(forms.ModelForm):

    parkingtype_list = [
        ('平面駐車場', '平面駐車場'),
        ('立体駐車場', '立体駐車場'),
    ]
    parking_type = forms.ChoiceField(choices=parkingtype_list, label='駐車場タイプ', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = ParkingUserModel
        fields = ['parking_type','width','length','height','count']
        widgets = {
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'width': '横幅(m)',
            'length': '奥行き(m)',
            'height': '高さ(m)',
        }


class UploadFileForm(forms.Form):
    file  = forms.FileField()