from django.shortcuts import render, get_object_or_404
from .models import BPost

def posts_list(request):
    # posts = BPost.objects.all()
    posts = BPost.objects.filter(status='p')
    context = {'postha': posts}
    return render(request, 'posts_list.html', context)

def show_detail(request, pk):
    post = get_object_or_404(BPost, pk=pk)
    return render(request, 'detail.html', {'post': post})
from .forms import NewPostForm
def new_post(request):
    form = NewPostForm()
    return render(request, 'new_post.html', {'form': form})