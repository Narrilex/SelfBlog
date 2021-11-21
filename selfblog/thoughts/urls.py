from django.urls import path
from django.urls.conf import re_path

from .views import *

urlpatterns = [
    path('', index, name = "glagna"),
    path('cats/<int:catid>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]