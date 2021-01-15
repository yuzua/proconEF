from django import forms
from django.core.mail import EmailMessage
from .models import CarsharUserModel
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime, re

class CarsharUserCreateForm(forms.ModelForm):
    # def __init__(self, *args, **kwd):
    #     super(CarsharUserCreateForm, self).__init__(*args, **kwd)
    #     self.fields["gender"].required = False
    GENDER_LIST = [
        (True, '男性'), 
        (False, '女性')
    ]
    gender = forms.ChoiceField(choices=GENDER_LIST, label='性別', widget=forms.Select(attrs={'class': 'form-control'}))
    CREDIT_CARD_COMPANY_LIST = [
        ('VISA', 'VISA'), 
        ('MasterCard', 'MasterCard'),
        ('JCB', 'JCB')
    ]
    credit_card_company = forms.ChoiceField(choices=CREDIT_CARD_COMPANY_LIST, label='カード会社', widget=forms.RadioSelect)


    class Meta:
        model = CarsharUserModel
        fields = ['id', 'gender', 'zip01', 'pref01', 'addr01', 'addr02', 'tel', \
            'credit_card_company', 'first_en', 'last_en', 'credit_card_num', 'valid_thru', 'security_code']
        widgets = {
            'zip01': forms.NumberInput(attrs={'class': 'form-control', 'onKeyUp' : "AjaxZip3.zip2addr(this,'','pref01','addr01')"}),
            'pref01': forms.TextInput(attrs={'class': 'form-control'}),
            'addr01': forms.TextInput(attrs={'class': 'form-control'}),
            'addr02': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'credit_card_company': forms.TextInput(attrs={'class': 'form-control'}),
            'first_en': forms.TextInput(attrs={'class': 'form-control'}),
            'last_en': forms.TextInput(attrs={'class': 'form-control'}),
            'credit_card_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'valid_thru': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'02/21'}),
            'security_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'plan': forms.TextInput(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control-file', 'required': 'True'})
        }
        labels={
            'first_name': '氏(漢字)',
            'last_name': '名(漢字)',
            'first_ja': '氏(ひらがな)',
            'last_ja': '名(ひらがな)',
            'gender': '性別',
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
            'plan': '利用プラン',
            'img': '免許証'
        }


class CarsharUserNameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CarsharUserNameForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    dt_now = datetime.datetime.now()
    min_year = dt_now.year - 20
    max_year = dt_now.year - 80

    first_name = forms.CharField(label='id_name', max_length=100)
    last_name = forms.CharField(label='id_name', max_length=100)
    first_ja = forms.CharField(label='id_ja', max_length=100)
    last_ja = forms.CharField(label='id_ja', max_length=100)
    birthday_year = forms.IntegerField(label='id_birthday_year', \
        validators=[MinValueValidator(max_year), MaxValueValidator(min_year)] )
    birthday_month = forms.IntegerField(label='id_birthday_month', \
        validators=[MinValueValidator(1), MaxValueValidator(12)] )
    birthday_day = forms.IntegerField(label='id_birthday_day', \
        validators=[MinValueValidator(1), MaxValueValidator(31)] )
    

    def clean_first_ja(self):
        first_ja = re.search(r'^[\u3041-\u309F]*$', self.cleaned_data['first_ja'])
        if first_ja is None:
            raise forms.ValidationError("ひらがなで入力して下さい。")
        return first_ja

    def clean_last_ja(self):
        last_ja = re.search(r'^[\u3041-\u309F]*$', self.cleaned_data['last_ja'])
        if last_ja is None:
            raise forms.ValidationError("ひらがなで入力して下さい。")
        return last_ja

class PhotoForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file', 'required': 'True'}))