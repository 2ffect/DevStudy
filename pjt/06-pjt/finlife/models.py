from django.db import models

# Create your models here.

class DepositProducts(models.Model):
    class JoinLimits(models.IntegerChoices):
        NOLIMIT = 1, '제한없음'
        SONLY = 2, '서민전용'
        SOMELIMIT = 3, '일부제한'
        
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField(choices=JoinLimits.choices)
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()    
    

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()