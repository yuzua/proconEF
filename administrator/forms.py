from django import forms
from parking_req .models import ParkingUserModel
from .models import MediaModel

class AdminParkingForm(forms.ModelForm):

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
        fields = ['parking_type','ground_type','width','length','height','count']
        widgets = {
            'width': forms.NumberInput(attrs={'class': 'form-control'}),
            'length': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'readonly':''}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'width': '横幅(m)',
            'length': '奥行き(m)',
            'height': '高さ(m)',
        }


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = MediaModel
        fields = ['attach']