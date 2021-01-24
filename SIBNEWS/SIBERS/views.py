from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import News


def index(request):
    qs = News.objects.all().order_by('-created_at')
    context = {'object_list': qs}
    return render(request, 'index.html', context)


def new_post(request):
    if request.method == "POST":
        post = News()
        post.headline = request.POST.get('headline')
        post.body = request.POST.get('body')
        post.created_at = datetime.today()
        post.save()
        return redirect('/index')
    else:
        form = PostForm()
        return render(request, 'new_post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    return render(request, 'post_detail.html', {'post': post})




