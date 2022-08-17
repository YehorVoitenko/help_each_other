from datetime import timezone, datetime

from django.db import models


class Post(models.Model):
    title = models.CharField('Enter title', max_length=50)
    description = models.TextField('Enter description')
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

