from .models import User
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 아이디
        self.fields['username'].label = '아이디'
        self.fields['username'].widget.attrs.update({
            'placeholder': '아이디 입력해주세요.',
            'class': 'form-control',
        })

        # 비밀번호
        self.fields['password1'].label = '비밀번호'
        self.fields['password1'].widget.attrs.update({
            'placeholder': '비밀번호 입력해주세요.',
            'class': 'form-control',
        })

        # 비밀번호 확인
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].widget.attrs.update({
            'placeholder': '비밀번호 확인해주세요.',
            'class': 'form-control',
        })
