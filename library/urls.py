from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter


routers=SimpleRouter()
routers.register('book',BookViewSet,basename='book')
routers.register('category',CategoryViewSet,basename='category')
routers.register('reader',ReaderViewSet,basename='reader')
routers.register('checkout',CheckoutViewSet,basename='checkout')
routers.register('transactions',TransactionsViewSet,basename='transactions')
routers.register('review',ReviewViewSet,basename='review')
urlpatterns = [

]+routers.urls
