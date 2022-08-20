from datetime import timezone, datetime
from phone_field import PhoneField

from django.db import models


class Post(models.Model):
    name = models.TextField('Enter your name', max_length=50, null=False)
    surname = models.TextField('Enter your surname', max_length=50, null=False)
    telephone_number = models.IntegerField(blank=True, help_text='Enter your telephone number', unique=True)

    title = models.TextField('Enter title', max_length=50, null=False)
    description = models.TextField('Enter description', null=False)
    city = models.TextField('Enter city, you live', max_length=50, null=False)

    image = models.FileField(blank=True, default='default_picture/default_picture.png', null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

