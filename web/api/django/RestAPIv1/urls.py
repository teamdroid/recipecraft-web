from django.urls import path

from RestAPIv1.views import RecipesList, Report, GetGoogleUser, CreateGoogleUser, AddGoogleUserFavoriteRecipes, \
    DeleteGoogleUserFavoriteRecipes

urlpatterns = [
    # """path('', )"""
    path('getRecipes/', RecipesList.as_view()),  # request to get all recipes #TODO:Change name of endpoint
    path('report/', Report.as_view()),
    path('google-user/<str:uid>/<str:token>/', GetGoogleUser.as_view()),
    path('google-user/<str:token>/', CreateGoogleUser.as_view()),
    path('google-user/add-recipes/<str:uid>/<str:token>/', AddGoogleUserFavoriteRecipes.as_view()),
    path('google-user/delete-recipes/<str:uid>/<str:token>/', DeleteGoogleUserFavoriteRecipes.as_view()),

]
