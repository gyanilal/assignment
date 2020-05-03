from django.shortcuts import render
import csv
from .serializer import *
# Create your views here.

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse
import tweepy
# class SignUpView(APIView):
# 	authentication_classes = [SessionAuthentication, BasicAuthentication]
# 	def post(self,request):
# 		username = self.request.data.get("email")
# 		password = self.request.data.get("password")
# 		if username is None or password is None:
# 			return Response({'success': False},status=HTTP_400_BAD_REQUEST)
# 		else:
# 			try:
# 				user = User.objects.get(username=username)
# 				if user:
# 					return Response({'success': False},status=HTTP_400_BAD_REQUEST)
# 			except:
# 				user = User.objects.create_user(username=username,password=password,
# 					email=username)
# 				return Response({'success': True},status=HTTP_200_OK)

# class LoginApi(APIView):
# 	authentication_classes = [SessionAuthentication, BasicAuthentication]
# 	def post(self,request):
# 		username = self.request.data.get("email")
# 		password = self.request.data.get("password")
# 		if username is None or password is None:
# 			return Response({'success': False},status=HTTP_400_BAD_REQUEST)
# 		else:
# 			user = User.objects.get(username=username)
# 			if not user:
# 				return Response({'success': False},status=HTTP_400_BAD_REQUEST)
# 			else:
# 				try:
# 					Token.objects.get(user=user).delete()
# 				except:
# 					token, created = Token.objects.get_or_create(user=user)
# 				return Response({'token': token.key},status=HTTP_200_OK)


# class CsvView(APIView):
# 	serializer_class = CsvSerializer
# 	def get_serializer(self, queryset, many=True):
# 		return self.serializer_class(queryset,many=many,)
# 	def get(self,request, *args, **kwargs):
# 		response = HttpResponse(content_type='text/csv')
# 		response['Content-Disposition'] = 'attachment; filename="export.csv"'
# 		queryset = User.objects.filter(is_staff=False)
# 		serializer = self.get_serializer(queryset, many=True)
# 		header = CsvSerializer.Meta.fields
# 		wp = csv.DictWriter(response, fieldnames=header)
# 		wp.writeheader()
# 		for i in serializer.data:
# 			wp.writerow(i)
# 		return response


class TwitterView(APIView):
	# def get_all_tweets()
	def get_all_tweets(self):
		consumerKey = "Y2x9rnSVirom9p4aP4j4GmWGy"
		consumerSecret = "peCyxeqB68YvMrcdjXilHbzbWe3KXZKD4cE6NzHnjxTd2GCm9u"
		accessToken = "2186053585-zX6VlzWtTr9nNg72SXk9q0TWe6yV6VDyI0TCaxF"
		accessTokenSecret = "T3NAV6vXeOzHXLwBRulUXyBxRQUP8cjdbepFkeFzQyMgh"
		auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
		auth.set_access_token(accessToken, accessTokenSecret)
		a = tweepy.API(auth)
		searchTerm = "@narendramodi"
		# new_tweets = a.user_timeline(screen_name = searchTerm,count=15)
		new_tweets = a.user_timeline(screen_name = searchTerm,count=15, tweet_mode="extended")
		for i in new_tweets:
			a = Tweet.objects.filter(tweet_id=i.id_str)
			if len(a) < 1:
				Tweet(title=i.full_text,tweet_id=int(i.id_str)).save()
				# print(i)
			else:
				pass

	def get(self,request):
		self.get_all_tweets()
		serializer_class = TweetSerializer
		queryset = Tweet.objects.all()[:15]
		serializer = TweetSerializer(queryset, many=True)
		return Response({'data': serializer.data },status=HTTP_200_OK)


