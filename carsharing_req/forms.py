from django import forms
from.models import CarsharUserModel

class CarsharUserCreateForm(forms.ModelForm):
    class Meta:
        model = CarsharUserModel
        fields = ['id', 'name', 'mail', 'gender', 'age', 'birthday', 'system_flag']