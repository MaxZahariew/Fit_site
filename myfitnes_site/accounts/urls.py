from django.urls import path

from accounts.views import (
    login_view,
    RegisterView,
    EmailVerificationsView
)

# app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('verify/<str:email>/<uuid:token>/', EmailVerificationsView.as_view(), name='email_verification'),
    path('verify/<str:email>/<uuid:token>/',
         EmailVerificationsView.as_view(), name='email_verification'),
]
