from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from RestAPIv1.models import Recipe
from RestAPIv1.serializers import RecipeSerializer, ReportMessageSerializer
from recipcraftApi.settings import DEBUG


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
