from django.urls import path, re_path
from base.views import index_view as i
urlpatterns = [
    path("", i.dummy_view)
]
