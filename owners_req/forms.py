from django import forms
from.models import CarsharOwnersModel

class CarsharOwnersCreateForm(forms.ModelForm):
    maker_list = [
        ()
    ]
    car_maker =

    car_type = 

    car_possible = forms.IntegerField(label='乗車可能人数',
        widget=forms.TextInput(attrs={'class':'form-control'}))
    car_number =　forms.IntegerField(label='ナンバープレート(数字のみ入力)',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
        
    bank_name =　

    bank_num = forms.IntegerField(label='支店番号',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    account_num = forms.IntegerField(label='口座番号',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    account_name = forms.CharField(label='口座名義名(カタカナ)', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = CarsharOwnersModel
        fields = ['id', 'car_maker', 'car_type', 'car_possible', 'car_number', \
                 'bank_name', 'bank_num', 'account_num', 'account_name']



   