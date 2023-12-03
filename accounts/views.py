from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# from . import models

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    
# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         if password1!=password2:
#             return render(request, 'registration/signup.html', {"error": "password1 and password2 does not match"})
#         models.Account.objects.create(username=username, password=password1)
#         return redirect('login')
#     return render(request, 'registration/signup.html')