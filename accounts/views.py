from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout  # 겹치니깐 이렇게 임포트
from django.views.decorators.http import require_POST

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # 회원가입로직
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('articles:index')
    else:   # == 'GET'
        form = UserCreationForm()
    context = { 'form': form }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        # 로그인로직
        form = AuthenticationForm(request, request.POST)    # 이거 시험
        if form.is_valid():
            auth_login(request, form.get_user())
            next_page = request.GET.get('next')
            return redirect(next_page or 'articles:index')
    else: # == 'GET'
        form = AuthenticationForm()    
        
    context = { 'form': form }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')