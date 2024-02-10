from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('genre',)
    search_fields=('genre',)




@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','publication_date','isbn','availability','pdf_file','category')
    list_filter=('author','category','availability',)
    search_fields=('title','author','category',)
    
    


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display=('first_name','middle_name','last_name','address','gender',)
    search_fields=('first_name',)
    list_per_page=5
    
    
    
    

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display=('reader','book','checkout_date','due_date',)
    search_fields=('reader','book',)
    autocomplete_fields=('book','reader',)
    list_filter=('reader','book','checkout_date','due_date',)
    
    
    
    

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display=('checkout','amount','transaction_type','date',)
    autocomplete_fields=('checkout',)
    search_fields=('transaction_type',)
    list_filter=('transaction_type','date',)
    
    
    
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('book','reader','rating',)
    list_filter=('rating',) 
    search_fields=('book',)   

