from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# 구글 로그인 관련 import
import os
import urllib.parse
import requests
from dotenv import load_dotenv
load_dotenv()

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('boards:index')

def profile(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    articles = person.board_set.all()
    comments = person.comment_set.all()
    followers = person.followers.all()
    context = {
        'person': person,
        'articles': articles,
        'comments': comments,
        'followers': followers,
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        # 요청한 사람의 페이지가 아닐 때만 기능 제공
        if request.user in person.followers.all():
            # 이미 팔로워 목록에 있으면
            # 언팔로우 기능
            person.followers.remove(request.user)
        else:
            # 아니면 팔로우 add
            person.followers.add(request.user)
    return redirect('accounts:profile', person.pk)



# 구글 로그인 요청 
def google_login(request):
    # client_id 가져오기 (.env)
    clinet_id = os.getenv("GOOGLE_CLIENT_ID")
    # 리다이렉션 URI -> Google 클라이언트에 작성 되어 있음
    redirect_uri = "http://127.0.0.1:8000/accounts/google/callback/"
    scope = "openid email profile"
    # 인가 코드 응답 요청
    response_type = "code"

    google_auth_url = (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        + urllib.parse.urlencode({
            "client_id" : clinet_id,
            "redirect_uri" : redirect_uri,
            "response_type" : response_type,
            "scope" : scope,
            "prompt" : "select_account",
        })
    )

    return redirect(google_auth_url)

# 구글 액세스 토큰 요청 
def get_access_token(code):
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code" : code,
        "client_id" : os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret" : os.getenv("GOOGLE_CLIENT_SECRET"),
        "redirect_uri" : "http://127.0.0.1:8000/accounts/google/callback/",
        "grant_type" : "authorization_code",
    }
    response = requests.post(token_url, data=data)
    token_data = response.json()
    access_token = token_data.get("access_token")
    return access_token

# 구글 사용자 정보 요청
def get_user_info(access_token):
    userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"
    userinfo_response = requests.get(
        userinfo_url,
        headers={"Authorization" : f"Bearer {access_token}"}
        )
    userinfo = userinfo_response.json()

    email = userinfo.get("email")
    name = userinfo.get("name")
    if not email:
        return redirect("/")
    
    return email, name

# 구글 인가 코드 수신
def google_callback(request):
    User = get_user_model()

    # Google 인가 코드 
    code = request.GET.get("code")
    if not code:
        print("제공 코드 없음")
        return redirect("accounts:google-login")
    
    # 엑세스 토큰 요청
    access_token = get_access_token(code)
    # 사용자 정보 요청
    email, name = get_user_info(access_token)

    # 사용자 생성 또는 로그인
    user, created = User.objects.get_or_create(
        username = email,
        defaults={"first_name" : name}
    )
    print(f'User: {user}')

    if created:
        print(f'회원 가입 완료. : {user}')
    else:
        print(f'기존 회원입니다. : {user}' )
    
    auth_login(request, user)

    return redirect("boards:index")