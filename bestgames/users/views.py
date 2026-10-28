from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'регистрация прошла успешно')
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

