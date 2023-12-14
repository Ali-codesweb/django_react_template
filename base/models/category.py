from django.db import models


class CategoryModel(models.Model):
    name = models.TextField(default="")
