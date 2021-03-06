from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question_text

	def get_absolute_url(self):
		return reverse('polls:option', kwargs={'pk': self.pk})
		#return HttpResponseRedirect(reverse('polls:option', kwargs={'pk': self.pk}))

	# def was_published_recently(self):
	# 	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <=self.pub_date <=now

class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text

class Voter(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
