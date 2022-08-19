from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here
from .forms import PostForm
from .models import Post


def register(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('warning')
        else:
            print('[ERROR]')
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'main/register.html', context)


def home_page(request):
    post = Post.objects.order_by('-id')
    return render(request, 'main/home_page.html', {'post': post})


def warning(request):
    return render(request, 'main/warning.html')


def index(request):
    return render(request, 'main/index.html')
