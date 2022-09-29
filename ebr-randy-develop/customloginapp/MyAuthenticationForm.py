from django import forms
from django.contrib.auth.forms import UsernameField

from django.contrib.auth.models import User,auth
from django.core.exceptions import ValidationError


class MyAuthenticationForm(forms.Form):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )




    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #     # user=auth.authenticate(username=username,password=password)
    #     # if user is not None:
    #     #     if user.is_superuser:
    #     #         raise ValidationError("Not admin")
    #     # if user is None:
    #     #     raise ValidationError("invalid data")
    #     return cleaned_data