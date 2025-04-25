from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

import requests


API_KEY = settings.API_KEY
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL
    params = {
        'auth' : API_KEY,
        'topFinGrpNo' : '020000',
        'pageNo' : 1,
    }

    response = requests.get(URL, params=params).json()
    products_data = response['result']['baseList']
    option_data = response['result']['optionList']
    
    # print(type(products_data)) # list
    # print(type(option_data))   # list

    # 리스트 순회하면서 상품 담기 ??
    for product in products_data:
        if DepositProducts.objects.filter(fin_prdt_cd=product['fin_prdt_cd']).exists():
            continue  # 이미 존재하면 스킵
        product_serializer = DepositProductsSerializer(data=product)
        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()


    for option in option_data:
        product_id= DepositProducts.objects.get(fin_prdt_cd = option['fin_prdt_cd'])
        option['product'] = product_id.id
        if not option.get('intr_rate'):
            option['intr_rate'] = -1
        if not option.get('intr_rate2'):
            option['intr_rate2'] = -1

        
        option_serializer = DepositOptionsSerializer(data=option)
        if option_serializer.is_valid(raise_exception=True):
            option_serializer.save(product = product_id)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'POST':
        # 정기예금 상품 추가
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        # 전체 정기예금 상품 목록 출력
        all_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    # fin_prdt_cd 에 해당하는 상품 찾기
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    # fin_prdt_cd 랑 연결된 옵션만 필터링
    options = DepositOptions.objects.filter(product=product)
    # 시리얼라이즈 
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def top_rate(request):
    # 최고 우대 금리가 가장 높은 애 찾아오기
    max_intr_rate2 = DepositOptions.objects.order_by('-intr_rate2').first()
    # 위 옵션을 갖는 상품 가져오기
    product = max_intr_rate2.product

    # 둘 다 각각 시리얼라이즈 하고 출력 ?
    product_serializer = DepositProductsSerializer(product)
    option_serializer = DepositOptionsSerializer(max_intr_rate2)

    return Response({
        'deposit_product' : product_serializer.data,
        'options' : option_serializer.data
    }, status=status.HTTP_200_OK)