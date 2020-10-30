from django import forms
from.models import CarsharOwnersModel

class CarsharOwnersCreateForm(forms.ModelForm):
    maker_list = [
        ('レクサス', 'レクサス'),
        ('トヨタ', 'トヨタ'),
        ('日産', '日産'),
        ('ホンダ', 'ホンダ'),
        ('マツダ', 'マツダ'),
        ('スバル', 'スバル'),
        ('スズキ', 'スズキ'),
        ('三菱', '三菱'),
        ('ダイハツ', 'ダイハツ'),
        ('いすゞ', 'いすゞ'),
        ('光岡自動車', '光岡自動車'),
        ('トミーカイラ', 'トミーカイラ'),
        ('ゼロスポーツ', 'ゼロスポーツ'),
        ('日野自動車', '日野自動車'),
        ('UDトラックス', '三菱ふそう'),
        ('GLM', 'GLM'),
        ('その他外国車', 'その他外国車'),
    ]
    car_maker = forms.ChoiceField(label='メーカー', choices=maker_list)
    type_list = [
        ()
    ]

    car_type = forms.ChoiceField(label='車種', choices=type_list)

    car_possible = forms.IntegerField(label='乗車可能人数',
        widget=forms.TextInput(attrs={'class':'form-control'}))
    car_number = forms.IntegerField(label='ナンバープレート(数字のみ入力)',\
        widget=forms.TextInput(attrs={'class':'form-control'}))

    name_list = [
        ()
    ]
    bank_name = forms.ChoiceField(label='銀行選択', choices=name_list)

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



   