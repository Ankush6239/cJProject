# myapp/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
