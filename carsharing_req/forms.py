from django import forms
from django.core.mail import EmailMessage
from.models import CarsharUserModel

class CarsharUserCreateForm(forms.ModelForm):
    class Meta:
        model = CarsharUserModel
        fields = ['id', 'name', 'email', 'gender', 'age', 'birthday', 'system_flag']

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['name']
        message = self.cleaned_data['name']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名: {0}\nメールアドレス: {1}\nメッセージ:\n{2}'.format(name, email, message)
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()