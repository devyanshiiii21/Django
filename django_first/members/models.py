from django.db import models


class Members(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

