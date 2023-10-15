from django.shortcuts import render
from .models import BPost

def posts_list(request):
    posts = BPost.objects.all()
    context = {'postha': posts}
    return render(request, 'posts_list.html', context)