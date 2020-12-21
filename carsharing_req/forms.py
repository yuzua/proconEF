from django import forms
from django.core.mail import EmailMessage
from .models import CarsharUserModel

class CarsharUserCreateForm(forms.ModelForm):
    # def __init__(self, *args, **kwd):
    #     super(CarsharUserCreateForm, self).__init__(*args, **kwd)
    #     self.fields["gender"].required = False
    GENDER_LIST = [
        (True, '男性'), 
        (False, '女性')
    ]
    gender = forms.ChoiceField(choices=GENDER_LIST)
    credit_card_company_list = [
        ('VISA', 'VISA'), 
        ('MasterCard', 'MasterCard'),
        ('JCB', 'JCB')
    ]
    credit_card_company = forms.ChoiceField(choices=credit_card_company_list)


    class Meta:
        model = CarsharUserModel
        # fields = ['id', 'first_name', 'last_name', 'first_ja', 'last_ja', 'gender', 'zip01', 'pref01', 'addr01', 'addr02', 'tel', \
        #     'credit_card_company', 'first_en', 'last_en', 'credit_card_num', 'valid_thru', 'security_code', \
        #     'plan']
        fields = ['id', 'zip01', 'pref01', 'addr01', 'addr02', 'tel', \
            'credit_card_company', 'first_en', 'last_en', 'credit_card_num', 'valid_thru', 'security_code', \
            'plan']
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'gender': forms.widgets.Select,
            # 'gender': forms.RadioSelect,
            'zip01': forms.NumberInput(attrs={'class': 'form-control', 'onKeyUp' : "AjaxZip3.zip2addr(this,'','pref01','addr01')"}),
            'pref01': forms.TextInput(attrs={'class': 'form-control'}),
            'addr01': forms.TextInput(attrs={'class': 'form-control'}),
            'addr02': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'credit_card_company': forms.TextInput(attrs={'class': 'form-control'}),
            'first_en': forms.TextInput(attrs={'class': 'form-control'}),
            'last_en': forms.TextInput(attrs={'class': 'form-control'}),
            'credit_card_num': forms.TextInput(attrs={'class': 'form-control'}),
            'valid_thru': forms.TextInput(attrs={'class': 'form-control'}),
            'security_code': forms.TextInput(attrs={'class': 'form-control'}),
            'plan': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels={
            'first_name': '氏(漢字)',
            'last_name': '名(漢字)',
            'first_ja': '氏(ひらがな)',
            'last_ja': '名(ひらがな)',
            'gender': '性別',
        #    'age': '年齢',
        #    'birthday': '生年月日',
            'zip01': '郵便番号',
            'pref01': '都道府県名',
            'addr01': '市町村',
            'addr02': 'それ以降の住所',
            'tel': '電話番号',
            'credit_card_company': 'カード会社', 
            'first_en': '氏(ローマ字)',
            'last_en': '名(ローマ字)', 
            'credit_card_num': 'カード番号', 
            'valid_thru': '使用期限(月/年)',
            'security_code': 'セキュリティーコード',
            'plan': '利用プラン'
        }