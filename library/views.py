from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    
    queryset=Category.objects.all()
    serializer_class=CategorySerializer




class BookViewSet(viewsets.ModelViewSet):
    
    queryset=Book.objects.select_related('category').all()
    serializer_class=BookSerializer
    
    
    
    
class ReaderViewSet(viewsets.ModelViewSet):
    
    queryset=Reader.objects.all()
    serializer_class=ReaderSerializer



class CheckoutViewSet(viewsets.ModelViewSet):
    
    queryset=Checkout.objects.all()
    serializer_class=CheckoutSerializer
    
    
    
class TransactionsViewSet(viewsets.ModelViewSet):
    
    queryset=Transactions.objects.all()
    serializer_class=TransactionsSerializer
    
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer