from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=['id','genre']
        
class SimpleCategorySerializer(serializers.ModelSerializer):
    
      class Meta:
        model=Category
        fields=['id','genre',]
        
        
        




class BookSerializer(serializers.ModelSerializer):
    
    category_id=serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
        ,source='category'
    )
    category=SimpleCategorySerializer(read_only=True)
    class Meta:
        model=Book
        fields=['id','title','author','publication_date','isbn','availability','pdf_file','category_id','category',]
        



class ReaderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Reader
        fields="__all__"
        
        
        
class CheckoutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Checkout
        fields="__all__" 
        
        
        
class TransactionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Transactions
        fields="__all__"
        
        
        
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Review
        fields="__all__"        
