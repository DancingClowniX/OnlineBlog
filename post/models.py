from django.db import models

# Create your models here.

class News (models.Model):
    blob = models.ImageField(upload_to="images/")
    text = models.CharField(max_length=150)
    date_public = models.DateTimeField(auto_now_add=True)