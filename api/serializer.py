from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
# class CsvSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ['id','email','first_name']


class TweetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tweet
		fields = ['id','title']




