from django.urls import path

from fitness_app import views


urlpatterns = [
    path('home/', view=views.HomeView.as_view(), name="home")
]
