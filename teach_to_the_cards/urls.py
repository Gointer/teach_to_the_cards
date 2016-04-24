"""teach_to_the_cards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from card.views import (
    CardListView, CardCreateView, CardDeleteView, 
    CardUpdateView, CardDetailView
)

urlpatterns = [
	url(r'^$', CardListView.as_view(), name='card-list'),
	url(r'^new$', CardCreateView.as_view(), name='new'),
	url(r'^delete/(?P<pk>\d+)$', CardDeleteView.as_view(), name='delete'),
	url(r'^update/(?P<pk>\d+)$', CardUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)$', CardDetailView.as_view(), name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
