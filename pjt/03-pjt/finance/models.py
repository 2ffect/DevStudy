# finance/models.py
from django.db import models

class StockComment(models.Model):
    company_name = models.CharField(max_length=255)  # 회사 이름
    stock_code = models.CharField(max_length=255)    # 종목 코드
    comment = models.TextField()                      # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 저장 일자 (자동으로 현재 시간으로 설정)

    def __str__(self):
        return f'{self.company_name} - {self.stock_code}'
