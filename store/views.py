from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product

@api_view(['GET'])
def view_products(request):
	products = Products.objects.all()
	results = [product.to_json() for product in products]
	return Response(data=results, status=status.HTTP_201_CREATED)
