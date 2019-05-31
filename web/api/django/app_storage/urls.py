from django.urls import path, re_path
from .views import StorageView, FileDelete

urlpatterns = [
    # """path('', )"""
    path('', StorageView.as_view(), name="storage"),
    re_path(r'^delete/(?P<pk>\d+)/$', FileDelete.as_view(), name="delete_file"),
]
