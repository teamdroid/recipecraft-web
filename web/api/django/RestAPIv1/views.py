from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from RestAPIv1.models import Recipe, GoogleUser
from RestAPIv1.serializers import RecipeSerializer, ReportMessageSerializer, GoogleUserWriteSerializer, \
    GoogleUserReadSerializer, GoogleUserDeleteRecipesSerializer, GoogleUserUpdateRecipesSerializer
from recipcraftApi.settings import DEBUG
from google.auth.transport import requests
from google.oauth2 import id_token


def google_token_check(uid, token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request())

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        if uid == idinfo['sub']:
            raise ValueError('Wrong UID')

        if idinfo['exp'] == 0:
            raise ValueError('The token has expired')
    except ValueError:
        return False
    return True

# Create your views here.
class RecipesList(APIView):
    """View for get all recipes"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


class Report(APIView):
    permission_classes = [permissions.AllowAny]
    if not DEBUG:
        throttle_scope = 'send_reports'  # limits 1 request per day

    def post(self, request):
        serializer = ReportMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetGoogleUser(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, uid, token):
        if not (google_token_check(uid, token)):
            return Response(data={"detail": "uid and token do not match"}, status=status.HTTP_401_UNAUTHORIZED)
        google_user = GoogleUser.objects.filter(uid=uid)
        serializer = GoogleUserWriteSerializer(google_user)
        return Response(serializer.data)


class CreateGoogleUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, token):
        if not (google_token_check(request.data['uid'], token)):
            return Response(data={"detail": "uid and token do not match"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = GoogleUserReadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddGoogleUserFavoriteRecipes(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, uid, token):
        if not (google_token_check(uid, token)):
            return Response(data={"detail": "uid and token do not match"}, status=status.HTTP_401_UNAUTHORIZED)

        google_user = GoogleUser.objects.filter(uid=uid)
        if google_user:
            google_user = google_user[0]
            serializer = GoogleUserUpdateRecipesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.update(google_user, serializer.validated_data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteGoogleUserFavoriteRecipes(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, uid, token):
        if not (google_token_check(uid, token)):
            return Response(data={"detail": "uid and token do not match"}, status=status.HTTP_401_UNAUTHORIZED)
        google_user = GoogleUser.objects.filter(uid=uid)
        if google_user:
            serializer = GoogleUserDeleteRecipesSerializer(data=request.data)
            google_user = google_user[0]
            if serializer.is_valid():
                serializer.update(google_user, serializer.validated_data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
