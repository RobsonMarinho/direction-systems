from django import forms
from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        # custom fileds
        self.fields['first_name'] = forms.CharField(required=True)
        self.fields['last_name'] = forms.CharField(required=True)

        # widgets
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].widget.attrs['class'] = 'form-control'

        self.fields['first_name'].widget.attrs['placeholder'] = 'Nome'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'

        self.fields['last_name'].widget.attrs['placeholder'] = 'Sobrenome'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs['placeholder'] = 'Email'
        self.fields['login'].widget.attrs['class'] = 'form-control'

        self.fields['password'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class CustomResetPasswordForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(CustomResetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['class'] = 'form-control'


class CustomPasswordResetConfirmForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetConfirmForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['placeholder'] = 'Nova senha'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'

        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirmar nova senha'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
