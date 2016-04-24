from django.conf.urls import url, include

from . import views


urlpatterns = [
	url(r'^$', views.CardListView.as_view(), name='list'),
	url(r'^new$', views.CardCreateView.as_view(), name='new'),
	url(r'^delete/(?P<pk>\d+)$', views.CardDeleteView.as_view(), name='delete'),
	url(r'^update/(?P<pk>\d+)$', views.CardUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)$', views.CardDetailView.as_view(), name='detail'),
]