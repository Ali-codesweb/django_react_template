from django.db import models


class PollsModel(models.Model):
    name = models.TextField(default="")
