from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here
from .forms import PostForm
from .models import Post


def give_help(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        else:
            print('[ERROR]')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'main/give_help.html', context)


def home_page(request):
    post = Post.objects.all()
    return render(request, 'main/home_page.html', {'post': post})
