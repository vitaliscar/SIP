from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ThemePreferenceForm

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ThemePreferenceForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ThemePreferenceForm(instance=user)
    return render(request, 'users/profile.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    form = AuthenticationForm(request=request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('users:profile')  # Puedes ajustar esta redirección
    return render(request, 'users/login.html', {'form': form})


from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir al login o a donde desees después del registro
            from django.urls import reverse
            from django.shortcuts import redirect
            return redirect(reverse('users:login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def password_reset(request):
    return render(request, 'users/password_reset.html')

def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'users/password_reset_confirm.html')

@login_required
def user_detail(request, pk):
    return render(request, 'users/user_detail.html')

def user_list(request):
    return render(request, 'users/user_list.html')
