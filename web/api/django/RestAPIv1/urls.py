from django.urls import path

from RestAPIv1.views import RecipesList

urlpatterns = [
    # """path('', )"""
    path('getRecipes/', RecipesList.as_view()),  # request to get all recipes

]
