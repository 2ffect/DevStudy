from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from contentfetch.models import UserStock
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST



User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('pjt04:stock_finder')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form  = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('pjt04:stock_finder')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('pjt04:stock_finder')


@login_required
def profile(request):
    user = request.user
    stocks = UserStock.objects.filter(user=user)
    context = {
        'user': user,
        'stocks': stocks,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def add_stock(request):
    if request.method == 'POST':
        stock_name = request.POST.get('stock_name', '').strip()

        if not stock_name:
            return redirect('accounts:profile')

        # 중복 확인 (대소문자 무시)
        if not UserStock.objects.filter(user=request.user, stock_name__iexact=stock_name).exists():
            UserStock.objects.create(
                user=request.user,
                stock_name=stock_name  # 여기서 StockData 여부와 무관하게 저장
            )

        return redirect('accounts:profile')
    
@require_POST
@login_required
def delete_stock(request):
    stock_name = request.POST.get('stock_name')

    if stock_name:
        UserStock.objects.filter(user=request.user, stock_name=stock_name).delete()

    return redirect('accounts:profile')