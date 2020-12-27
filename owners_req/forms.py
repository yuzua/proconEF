from django import forms
from datetime import date
from.models import HostUserModel, CarInfoModel
from parking_booking .models import ParkingBookingModel
import bootstrap_datepicker_plus as datetimepicker
from.models import *


class HostUserForm(forms.ModelForm):
    
    class Meta:
        model = HostUserModel
        fields = ['bank_code', 'branch_code', 'bank_account_number']
        widgets = {
            'day': forms.DateInput(attrs={'class': 'form-control'}),
            'bank_code': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank_account_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'day': '登録日',
            'bank_code': '銀行コード',
            'branch_code': '支店コード',
            'bank_account_number': '口座番号'
        }



class CarInfoForm(forms.ModelForm):
    # 親カテゴリの選択欄がないと絞り込めないので、定義する。
    parent_category = forms.ModelChoiceField(
        label='メーカー',
        queryset=ParentCategory.objects,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        # super(CarsharUserCreateForm, self).__init__(*args, **kwd)
        # self.fields["img"].widget.attrs['class'] = 'form-control-file'
        self.fields["vehicle_inspection_day"].widget.attrs['placeholder'] = '2021-01-01'

    class Meta:
        model = CarInfoModel
        fields = ['parent_category', 'category', 'license_plate_place', 'license_plate_type', 'license_plate_how', 'license_plate_num', \
            'model_id', 'people', 'tire', 'used_mileage', \
            'used_years', 'vehicle_inspection_day']
        # fields = '__all__'
        # field_order = ('parent_category', 'category', 'license_plate', 'model_id', 'people', \
        #      'tire', 'used_years', 'vehicle_inspection_day')
        widgets = {
            'vehicle_inspection_day': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ).start_of('次回車検予定日'),
            'babysheet': forms.TextInput(attrs={'class': 'form-check'}),
        }

        labels = {
            #'user_id': 'ユーザID',
            'license_plate_place': 'ナンバープレート(地名)',
            'model_id': '型番',
            'people': '乗車人数',
            # 'day': '登録日',
            'tire': 'タイヤ',
            'used_years':'使用年数',
            'vehicle_inspection_day':'次回車検予定日'
        }
class CarOptionForm(forms.ModelForm):
    ATMT_LIST = [
        ('AT', 'AT'), 
        ('MT', 'MT')
    ]
    at_mt = forms.ChoiceField(
        choices=ATMT_LIST, 
        label='AT車 or MT車', 
        widget=forms.RadioSelect
    )

    class Meta:
        model = CarInfoModel
        fields = ['at_mt', 'babysheet', 'car_nav', 'etc', 'car_autonomous', 'around_view_monitor', 'non_smoking']
        field_order = ('at_mt', 'babysheet', 'car_nav', 'etc', 'around_view_monitor', 'car_autonomous', 'non_smoking')
        widgets = {
            'babysheet': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'car_nav': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'etc': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'around_view_monitor': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'car_autonomous': forms.CheckboxInput(attrs={'class': 'form-check'}),
            'non_smoking': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }
        labels = {
            'babysheet': 'チャイルドシート付き',
            'car_nav': 'カーナビ付き', 
            'etc': 'ETC付き', 
            'around_view_monitor': '駐車アシスト機能付き',
            'car_autonomous': '自動運転',
            'non_smoking': '禁煙車両'
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
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'car_id': forms.TextInput(attrs={'class': 'form-control'}),
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
   

   