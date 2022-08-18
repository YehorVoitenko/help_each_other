from .models import Post
from django.forms import ModelForm, TextInput, Textarea, ImageField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'surname', 'telephone_number',
                  'title', 'description', 'city', 'key_help_words']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Enter your name',
                'class': "form-control",
                'id': 'name'
            }),

            'surname': TextInput(attrs={
                'placeholder': 'Enter your surname',
                'class': "form-control",
                'id': 'surname'
            }),

            'telephone_number': TextInput(attrs={
                'placeholder': 'Enter your telephone number',
                'class': "form-control",
                'id': 'telephone_number'
            }),

            'title': TextInput(attrs={
                'placeholder': "Enter title",
                'class': "form-control",
                'id': 'title',

            }),

            'description': Textarea(attrs={
               'placeholder': "Enter description (200 symbols)",
               'class': "form-control",
               'id': 'description'
                   }),

            'city': TextInput(attrs={
               'placeholder': "Enter city, you live",
               'class': "form-control",
               'id': 'city'
                   }),

            'key_help_words': TextInput(attrs={
               'placeholder': "A few key words, for easier search example: table, chair, toys",
               'class': "form-control",
               'id': 'key_help_words'
                   }),
        }
