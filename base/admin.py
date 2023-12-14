from django.contrib import admin
from .models import CategoryModel, PollsModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(PollsModel)
