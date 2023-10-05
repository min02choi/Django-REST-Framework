from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# 기존 장고 방식
def hello_world(request):
    return render(request, 'accountapp/temp.html')


# DRF 방식
# key-value 쌍으로
@api_view()
def hello_world_drf(request):
    return Response({'message': 'Hello DRF'})
