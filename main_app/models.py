from django.db import models

# Create your models here.
class Test(models.Model):
    test_field = models.TextField(max_length=500)