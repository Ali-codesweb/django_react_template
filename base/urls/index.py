from django.urls import path, re_path
from base.views import index as i
urlpatterns = [
    path("", i.dummy_view)
]
