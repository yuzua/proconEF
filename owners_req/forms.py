from django import forms
from datetime import date
from.models import HostUserModel

from.models import *


class HostUserForm(forms.ModelForm):
    
    # day = forms.DateField(label='登録日', \
    #      widget=forms.TextInput(attrs={'class':'form-control'}))
    pay_list = [
        ('銀行振込','銀行振込'),
        ('QR決済','QR決済'),
    ]
    pay = forms.ChoiceField(choices=pay_list)
    # bank_name = forms.CharField(label='銀行名', \
    #      widget=forms.TextInput(attrs={'class':'form-control'}))
    # bank_code = forms.IntegerField(label='支店コード',\
    #     widget=forms.TextInput(attrs={'class':'form-control'}))
    # bank_account_number = forms.IntegerField(label='口座番号',\
    #     widget=forms.TextInput(attrs={'class':'form-control'}))
    # QR_id = forms.CharField(label='QR決済ID', \
    #     widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = HostUserModel
        fields = ['pay', 'bank_name', 'bank_code', \
             'bank_account_number', 'QR_id']
        widget = {
            'user_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'day': forms.DateInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_account_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'QR_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'user_id': 'ユーザID',
            'day': '登録日',
            'pay': '支払方法',
            'bank_name': '銀行名(カタカナ）',
            'bank_code': '支店コード',
            'bank_account_number': '口座番号',
            'QR_id': 'QR決済ID',
        }


# class CarInfoForm(forms.ModelForm):

    # license_plate = forms.IntegerField(label='ナンバープレート',\
    #     widget=forms.TextInput(attrs={'class':'form-control'}))    	
    # ParentCategory = forms.ChoiceField(label='メーカー', )
    # category = forms.ChoiceField(label='車種', )
    # model_id = forms.IntegerField(label='型番',\
    #     widget=forms.TextInput(attrs={'class':'form-control'}))
    # custom = forms.CharField(label='カスタム', \
    #     widget=forms.TextInput(attrs={'class':'form-control'}))	
    # people = forms.IntegerField(label='乗車人数',\
    #     widget=forms.TextInput(attrs={'class':'form-control'})) 
    # day = forms.DateField(label='登録日', \
    #      widget=forms.TextInput(attrs={'class':'form-control'}))
    # tire = forms.CharField(label='タイヤ', \
    #     widget=forms.TextInput(attrs={'class':'form-control'}))	
    # used_years =  forms.IntegerField(label='使用年数',\
    #     widget=forms.TextInput(attrs={'class':'form-control'}))
    # vehicle_inspection_day = forms.DateField(label='次回車検予定日', \
    #      widget=forms.TextInput(attrs={'class':'form-control'}))

    # class Meta:
    #     model = CarInfoModel
    #     fields = ['id', 'license_plate', 'model_id', 'custom', 'people', \
    #     'day', 'tire', 'used_years',  'vehicle_inspection_day']
        
        

class PostCreateForm(forms.ModelForm):
    # 親カテゴリの選択欄がないと絞り込めないので、定義する。
    parent_category = forms.ModelChoiceField(
        label='メーカー',
        queryset=ParentCategory.objects,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'

    field_order = ('parent_category', 'category', 'license_plate', 'model_id', 'custom', 'people', \
         'day', 'tire', 'used_years', 'vehicle_inspection_day')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


        # widget = {
            
        #     'license_plate': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'model_id': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'custom': forms.TextInput(attrs={'class': 'form-control'}),
        #     'people': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'day': forms.DateInput(attrs={'class': 'form-control'}),
        #     'tire': forms.TextInput(attrs={'class': 'form-control'}),
        #     'used_years': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'vehicle_inspection_day': forms.DateInput(attrs={'class': 'form-control'}),
        # }
        labels = {
            'license_plate': 'ナンバープレート',
            'model_id': '型番',
            'custom': 'カスタム',
            'people': '乗車人数',
            'day': '登録日',
            'tire': 'タイヤ',
            'used_years':'使用年数',
            'vehicle_inspection_day':'次回車検予定日'
        }

   