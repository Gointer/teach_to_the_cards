from django.core.urlresolvers import reverse
from django.db import models


class Card(models.Model):
	question = models.TextField(unique=True)
	answer = models.TextField()
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question

	def get_absolute_url(self):
		return reverse('card:detail', args=[self.id])
