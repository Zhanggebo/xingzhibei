from django import forms
from django.core.validators import RegexValidator


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字')],min_length=8,max_length=11)
