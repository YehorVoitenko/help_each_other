from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here
from .forms import PostForm
from .models import Post


def homepage(request):
    return render(request, 'main/home_page.html')


def give_help(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receive_help')
        else:
            print('[ERROR]')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'main/give_help.html', context)


def receive_help(request):
    post = Post.objects.all()
    return render(request, 'main/receive_help.html', {'post': post})


def base(request):
    return render(request, 'main/base.html')
