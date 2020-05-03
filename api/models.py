from django.db import models

# Create your models here.

class Tweet(models.Model):
	id = models.AutoField(primary_key=True)
	tweet_id = models.IntegerField(default=0)
	title = models.CharField(max_length=2000)

	def __str__(self):
		return self.tweet_id
