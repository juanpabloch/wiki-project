from django.db import models

# Create your models here.
class New_Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()