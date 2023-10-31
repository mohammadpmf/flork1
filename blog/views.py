from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import BPost
from .forms import NewPostForm

def posts_list(request):
    # posts = BPost.objects.all()
    posts = BPost.objects.filter(status='p').order_by('-datetime_modified')
    context = {'postha': posts}
    return render(request, 'posts_list.html', context)

def show_detail(request, pk):
    post = get_object_or_404(BPost, pk=pk)
    return render(request, 'detail.html', {'post': post})

def new_post(request):
    form = NewPostForm()
    if request.method=='POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            form = NewPostForm()
            return redirect(reverse("blog"))
    return render(request, 'new_post.html', {'form': form})