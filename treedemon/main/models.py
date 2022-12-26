from django.db import models


class TreeModel(models.Model):
    item = models.CharField(max_length=500)
    lft = models.IntegerField()
    rgt = models.IntegerField()
