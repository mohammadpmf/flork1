from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import BPost, Comment
from .forms import NewPostForm
from django.views import generic

class PostsList(generic.ListView):
    model = BPost
    template_name='posts_list.html'
    context_object_name = 'postha'

    def get_queryset(self):
        return BPost.objects.filter(status='p').order_by('-datetime_modified')

# def posts_list(request):
#     # posts = BPost.objects.all()
#     posts = BPost.objects.filter(status='p').order_by('-datetime_modified')
#     context = {'postha': posts}
#     return render(request, 'posts_list.html', context)

def show_detail(request, pk):
    post = get_object_or_404(BPost, pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method=='POST':
        author_name = request.POST.get('author_name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        Comment.objects.create(author=author_name, email=email, text=text, post=post)
    return render(request, 'detail.html', {'post': post, 'comments': comments})

class NewPost(generic.CreateView):
    model = BPost
    template_name = 'new_post.html'
    form_class = NewPostForm
    context_object_name = 'form'

# def new_post(request):
#     form = NewPostForm()
#     if request.method=='POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = NewPostForm()
#             return redirect(reverse("blog"))
#     return render(request, 'new_post.html', {'form': form})

class UpdatePost(generic.UpdateView):
    model = BPost
    template_name = 'new_post.html'
    form_class = NewPostForm
    context_object_name = 'form'

# def update_post(request, pk):
#     post = get_object_or_404(BPost, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse("blog"))
#     return render(request, 'new_post.html', {'form': form})

class DeleteView(generic.DeleteView):
    model = BPost
    template_name = 'delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog')

# def delete_post(request, pk):
#     post = get_object_or_404(BPost, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('blog')
#     return render(request, 'delete_post.html' , {'post': post})
