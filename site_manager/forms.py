from .models import Post
from django.forms import ModelForm, TextInput, Textarea, ImageField


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
        widgets = {'title': TextInput(attrs={'placeholder': "Enter title"}),
                   'description': Textarea(attrs={'placeholder': "Enter description"})
                   }
