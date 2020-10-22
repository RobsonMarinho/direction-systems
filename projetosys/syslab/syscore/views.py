from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .forms import CustomLoginForm, CustomSignupForm, CustomResetPasswordForm, CustomPasswordResetConfirmForm
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from allauth.account.views import SignupView, LoginView, EmailVerificationSentView


# user section
class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = CustomLoginForm


class Signup(SignupView):
    template_name = 'account/register.html'
    form_class = CustomSignupForm




# password reset section
class CustomPasswordResetView(PasswordResetView):
    html_email_template_name = 'account/password_reset_email.html'
    from_email = 'joastestesys@gmail.com'
    title = 'Alteração de Senha'
    template_name = 'account/password_reset_form.html'
    form_class = CustomResetPasswordForm


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    form_class = CustomPasswordResetConfirmForm


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


class customEmailVerificationSentView(EmailVerificationSentView):
    pass


# pages system

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'home/secret_page.html'

