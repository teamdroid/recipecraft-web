from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from RestAPIv1.models import Recipe
from RestAPIv1.serializers import RecipeSerializer


# Create your views here.
class RecipesList(APIView):
    """View for get all recipes"""
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
