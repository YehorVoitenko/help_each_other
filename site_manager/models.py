from datetime import timezone, datetime

from django.db import models


class Post(models.Model):
    name = models.CharField('Enter your name', max_length=50, null=False)
    surname = models.CharField('Enter your surname', max_length=50, null=False)
    telephone_number = models.CharField('Enter your telephone number', max_length=50, null=False)

    title = models.CharField('Enter title', max_length=50, null=False)
    description = models.TextField('Enter description', null=False)
    city = models.CharField('Enter city, you live', max_length=50, null=False)
    key_help_words = models.CharField('Enter key words', max_length=50, null=False)

    image = models.FileField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

