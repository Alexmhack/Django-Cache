from django.urls import path

from .views import view_products

app_name = 'store'

urlpatterns = [
	path('', view_products, name='products'),
]
