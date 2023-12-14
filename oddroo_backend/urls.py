from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from .views import register_user, MyTokenObtainPairView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('admin', admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
    path('api/register',  register_user, name='register-user'),
    path('api/login', MyTokenObtainPairView.as_view(), name='login'),
    path('api/base/', include("base.urls.index")),
    # redirect all other urls to react
    re_path(r".*", TemplateView.as_view(template_name="index.html"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
