from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Card


class CardListView(ListView):
	model = Card
	template_name = 'homepage.html'


class CardCreateView(CreateView):
	model = Card
	template_name = 'create_card.html'
	success_url = '/'
	fields = ['question', 'answer']