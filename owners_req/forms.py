from django import forms
from datetime import date
from.models import HostUserModel, CarInfoModel

class HostUserForm(forms.ModelForm):
    
    day = forms.DateField(label='登録日', \
         widget=forms.TextInput(attrs={'class':'form-control'}))
    pay_list = [
        ('銀行振込','銀行振込'),
        ('QR決済','QR決済'),
    ]
    pay = forms.ChoiceField(label='支払方法', choices=pay_list)
    bank_name = forms.CharField(label='銀行名', \
         widget=forms.TextInput(attrs={'class':'form-control'}))
    bank_code = forms.IntegerField(label='支店コード',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    bank_account_number = forms.IntegerField(label='口座番号',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    QR_id = forms.CharField(label='QR決済ID', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = HostUserModel
        fields = ['id', 'day', 'pay', 'bank_name', 'bank_code', \
             'bank_account_number', 'QR_id']


class CarInfoForm(forms.ModelForm):
    
    license_plate = forms.IntegerField(label='ナンバープレート',\
        widget=forms.TextInput(attrs={'class':'form-control'}))    	
    ParentCategory = forms.ChoiceField(label='メーカー', )
    category = forms.ChoiceField(label='車種', )
    model_id = forms.IntegerField(label='型番',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    custom = forms.CharField(label='カスタム', \
        widget=forms.TextInput(attrs={'class':'form-control'}))	
    people = forms.IntegerField(label='乗車人数',\
        widget=forms.TextInput(attrs={'class':'form-control'})) 
    day = forms.DateField(label='登録日', \
         widget=forms.TextInput(attrs={'class':'form-control'}))
    tire = forms.CharField(label='タイヤ', \
        widget=forms.TextInput(attrs={'class':'form-control'}))	
    used_years =  forms.IntegerField(label='使用年数',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    vehicle_inspection_day = forms.DateField(label='次回車検予定日', \
         widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = CarInfoModel
        fields = ['id', 'license_plate', 'ParentCategory', 'category', \
            'model_id', 'custom', 'people', 'day', 'tire', 'used_years', \
            'vehicle_inspection_day']

   