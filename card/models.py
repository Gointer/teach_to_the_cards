from django.db import models


class Card(models.Model):
	question = models.TextField(unique=True)
	answer = models.TextField()

	