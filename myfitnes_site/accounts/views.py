import uuid
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect


from accounts.models import EmailVerification
from common.mixins import TitleMixin

from .forms import UserRegistrationsForm

from datetime import timedelta

# Create your views here.

User = get_user_model()


class RegisterView(SuccessMessageMixin, FormView):
    form_class = UserRegistrationsForm
    template_name = "account/register.html"
    success_url = reverse_lazy("login")
    succes_message = "You have successfully registered!"
    title = "Registrations"

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data["password"])
        new_user.save()

        expiration = timezone.now() + timedelta(days=2)
        token = uuid.uuid4()
        record = EmailVerification.objects.create(
            user=new_user, token=token, expiration=expiration
        )
        record.send_verification_email()

        return super().form_valid(form)


class ProfileUpdateView:
    pass


class EmailVerificationsView(TitleMixin, TemplateView):
    template_name = "email/email_verification.html"
    title = "Email Verification"

    def get(self, request, *args, **kwargs):
        token = kwargs["token"]
        email = kwargs["email"]

        user = User.objects.get(email=email)
        email_verification = EmailVerification.objects.filter(user=user, token=token)

        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified = True
            user.save()
            return super().get(request, *args, **kwargs)
        return redirect("home")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        muyser = authenticate(username=email, password=password)
        if muyser is not None:
            login(request, muyser)
            messages.success(request, "Пользователь успешно вошел в аккаунт")
            return redirect("home")
        else:
            messages.success(request, "Сouldn't log in to your account")
            return redirect("login")

    return render(request, "account/login.html")


def logout_view(request):
    pass
