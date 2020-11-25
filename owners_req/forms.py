from django import forms
from datetime import date
from.models import HostUserModel
import bootstrap_datepicker_plus as datetimepicker
from.models import *


class HostUserForm(forms.ModelForm):
    pay_list = [
        ('銀行振込','銀行振込'),
        ('QR決済','QR決済'),
    ]
    pay = forms.ChoiceField(choices=pay_list)
    
    class Meta:
        model = HostUserModel
        fields = ['pay', 'bank_name', 'bank_code', \
             'bank_account_number', 'QR_id']
        widget = {
            #'user_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'day': forms.DateInput(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'QR_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            #'user_id': 'ユーザID',
            'day': '登録日',
            'pay': '支払方法',
            'bank_name': '銀行名(カタカナ）',
            'bank_code': '支店コード',
            'bank_account_number': '口座番号',
            'QR_id': 'QR決済ID',
        }



class CarInfoForm(forms.ModelForm):
    # 親カテゴリの選択欄がないと絞り込めないので、定義する。
    parent_category = forms.ModelChoiceField(
        label='メーカー',
        queryset=ParentCategory.objects,
        required=False
    )

    class Meta:
        model = CarInfoModel
        fields = ['parent_category', 'category', 'license_plate', 'model_id', 'custom', 'people', \
         'tire', 'used_years', 'vehicle_inspection_day']
        #fields = '__all__'

    field_order = ('parent_category', 'category', 'license_plate', 'model_id', 'custom', 'people', \
         'tire', 'used_years', 'vehicle_inspection_day')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


        labels = {
            #'user_id': 'ユーザID',
            'license_plate': 'ナンバープレート',
            'model_id': '型番',
            'custom': 'カスタム',
            'people': '乗車人数',
            'day': '登録日',
            'tire': 'タイヤ',
            'used_years':'使用年数',
            'vehicle_inspection_day':'次回車検予定日'
        }


class CarInfoParkingForm(forms.ModelForm):
    class Meta:
        model = CarInfoParkingModel
        fields = ['car_id', 'parking_id', ]
    field_order = ('car_id', 'parking_id')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        labels = {
            'user_id': 'ユーザID',
            'car_id': '車両ID',
            'parking_id': '駐車場ID',
        }

class CarsharingDateForm(forms.ModelForm):

    class Meta:
        model = CarsharingDateModel
        fields = ['car_id', 'possible_date']
        widgets = {
            'possible_date': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }
        labels = {
            #'user_id': 'ユーザID',
            'car_id': '車両ID',
            'possible_date': '貸出可能日',
        }
   

   