from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password
import logging

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		print("YYY UserLogin")
		logging.debug("XXX UserLogin")

		#XXX send notification to React
		channel_layer = get_channel_layer()
		async_to_sync(channel_layer.group_send)(
            'notifications',  # Here 'notifications' is the group name that you have used in your consumer
            {
                'type': 'notification_message',
                'text': 'User logged in',
            }
        )

		return Response({"email": "a@gmail.com"}, status=status.HTTP_200_OK)
		# data = request.data
		# assert validate_email(data)
		# assert validate_password(data)
		# serializer = UserLoginSerializer(data=data)
		# if serializer.is_valid(raise_exception=True):
		# 	user = serializer.check_user(data)
		# 	login(request, user)
		# 	return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		print("YYY UserLogout")
		logging.debug("XXX UserLogout")
		logout(request)
		return Response(status=status.HTTP_200_OK)


class UserView(APIView):
	#permission_classes = (permissions.IsAuthenticated,)
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		print("YYY UserView")
		logging.debug("XXX UserView")
		return Response({'user': "a@gmail.com"}, status=status.HTTP_200_OK)
		# serializer = UserSerializer(request.user)
		# return Response({'user': serializer.data}, status=status.HTTP_200_OK)









