# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Products,Shopeeuser
from rest_framework import status

@api_view(['GET'])
def authenticateuser(request,uname,passwd):
    try:
        user = Shopeeuser.objects.get(username=uname,password=passwd)
    except Shopeeuser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return HttpResponse(status=200)

@api_view(['POST'])
def feed_product(request, id,name,category,price):
	
	if request.method == 'POST' :
		try:
			product = Products.objects.get(id=id)
			return HttpResponse(status=HTTP_409_CONFLICT)
		except Products.DoesNotExist:
			product = Products(id=id,name=name,category=category,price=price)
	    	product.save()
	    	return HttpResponse(status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_product(request, id,name,category,price):
	
	if request.method == 'PUT' :
		try:
			product = Products.objects.filter(id=id).update(name=name,category=category,price=price)
			product.save()
			return HttpResponse(status=status.HTTP_201_CREATED)
			
		except Products.DoesNotExist:
			return HttpResponse(status=HTTP_204_NO_CONTENT)
	    	


@api_view(['GET','DELETE'])
def product_id(request, id):
    try:
        product = Products.objects.get(id=id)
    except Products.DoesNotExist:
    	content = {'please move along': 'nothing to see here'}
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'DELETE' :
    	product.delete()
    	return HttpResponse(status=status.HTTP_200_OK)

@api_view(['GET'])
def product_name(request, name):
    try:
        product = Products.objects.get(name=name)
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@api_view(['GET'])
def product_category(request, category):
    try:
        product = Products.objects.get(category=category)
    except Products.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)