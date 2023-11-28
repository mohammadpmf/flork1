from django.db import models
from django.urls import reverse

class BPost(models.Model):
    STATUS_CHOICES = (
        ('p', 'published'),
        ('d', 'draft'),
    )
    title = models.CharField(max_length=60)
    text = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("show_detail", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, blank=True, null=True)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(to=BPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.text}"
