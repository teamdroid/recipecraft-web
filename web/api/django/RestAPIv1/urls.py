from django.urls import path

from RestAPIv1.views import RecipesList,Report

urlpatterns = [
    # """path('', )"""
    path('getRecipes/', RecipesList.as_view()),  # request to get all recipes
    path('report/', Report.as_view()),
]
