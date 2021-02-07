from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.models import Account
from django.contrib.auth.models import auth
from accounts.api.serializers import RegistrationSerializers, AuthSerializers
from rest_framework.authtoken.models import Token
from django.shortcuts import render
#pip install requests
import requests
import json
# @csrf_exempt
@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializers(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['message'] = 'successfully registered new user.'
			data['login_type'] = 'signup'
			data['user_id'] = account.id
			data['email'] = account.email
			data['first_name'] = account.first_name
			data['last_name'] = account.last_name
			token = Token.objects.get(user=account).key
			data['token'] = token
			# data['username'] = account.username
		else: 
			data = serializer.errors
		return Response(data)
# @csrf_exempt
# @api_view(['GET,'])
# def logout_view(request):
# 	auth.logout(request)
# 	response1={}
# 	response1['login_type'] = "logout"
# 	return Response(response1)



@api_view(['POST',])
def login_view(request):
	# serializer = AuthSerializers(data=request.data)
	email=request.data.get("email")
	password=request.data.get("password")
	response1={}
	if Account.objects.filter(email=email).exists():
		u = Account.objects.get(email=email)
		# raise serializers.ValidationError({
		# 	'user_id': u.id,
		# 	'login_type': "signin", 
		# })
		response1['user_id'] = u.id
		response1['login_type'] = "signin"
		user = auth.authenticate(username=email,password=password)
		if user is not None:
			auth.login(request,user)
			response1['meassage'] = "login successful"
		else:
			response1['message'] = "failed"
	else: 
		response1['user_id'] = "not registered"
		response1['login_type'] = "signup"
		
	# print(serializer)
	# if serializer.is_valid():
	# 	print("fuckkkkkkk")
	# 	email = serializer.save()
	# 	data['email'] = email 
	# else: 
	# 	data = serializer.errors
	return Response(response1)
# class ExampleView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)

