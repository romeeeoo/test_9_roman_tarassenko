from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label="username")
    password = forms.CharField(required=True, label="password", widget=forms.PasswordInput)

