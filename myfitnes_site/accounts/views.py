import uuid
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView, DetailView
from django.contrib.messages.views import SuccessMessageMixin

from accounts.models import EmailVerification

from .forms import UserRegistrationsForm

from datetime import timedelta
# Create your views here.


class RegisterView(SuccessMessageMixin, FormView):
    form_class = UserRegistrationsForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    succes_url = 'You have successfully registered!'
    title = 'Registrations'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()

        expiration = timezone.now() + timedelta(days=2)
        token = uuid.uuid4()
        record = EmailVerification.objects.create(
            user=new_user, token=token, expiration=expiration)
        record.send_verification_email()

        return super().form_valid(form)
