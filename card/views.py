from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Card


class CardListView(ListView):
	model = Card
	template_name = 'list_card.html'


class CardCreateView(CreateView):
	model = Card
	template_name = 'create_card.html'
	success_url = reverse_lazy('card:list')
	fields = ['question', 'answer', 'description',]


class CardDeleteView(DeleteView):
	model = Card
	template_name = 'delete_card.html'
	success_url = reverse_lazy('card:list')


class CardUpdateView(UpdateView):
	model = Card
	template_name = 'update_card.html'
	success_url = reverse_lazy('card:list')	
	fields = ['question', 'answer', 'description',]


class CardDetailView(DetailView):
	model = Card
	template_name = 'detail_card.html'
	context_object_name = 'card'
