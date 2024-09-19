from django.shortcuts import render
from django.views.generic.base import TemplateView, View

from action.mixins import TitleMixin


# Create your views here.
class HomeView(TitleMixin, TemplateView):
    '''Home index'''
    template_name = 'fitness_app/home.html'
    title = 'Main'