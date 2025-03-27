from django.db import models
import requests

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbeff2ct1139002'
# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    description = models.TextField()
    salesPoint = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    # Create your views here.
    def books_search(cls):
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'MaxResults': '20',
            'start': '1',
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101'
        }

        response = requests.get(API_URL, params=params).json()
        for item in response['item']:
            add_book = cls(isbn = item['isbn'], author = item['author'], title = item['title'],
                           description = item['description'], salesPoint = item ['salesPoint'],
                           price = item['priceSales'], fixed_price = item['fixedPrice'], pub_date = item['pubDate'])
            add_book.save()
