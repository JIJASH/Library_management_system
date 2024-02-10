from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

User=get_user_model()

class Category(models.Model):
    genre=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.genre




class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    publication_date=models.DateField()
    isbn=models.CharField(max_length=20)
    availability=models.CharField(max_length=20)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    



class Reader(models.Model):
    first_name=models.CharField(max_length=50,blank=True,null=True)
    middle_name=models.CharField(max_length=50,blank=True,null=True)
    last_name=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    
    GENDER_CHOICES=[
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHER'),
    ]
    
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True, null=True
    )
    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.first_name}({self.user.email})"
    
    
    

class Checkout(models.Model):
    reader=models.ForeignKey(Reader,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    checkout_date=models.DateTimeField(default=timezone.now)
    due_date=models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.book.title} - {self.reader.user.username}"
    
    
    
    

class Transactions(models.Model):
    checkout = models.OneToOneField(Checkout, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    PAYMENT_CHOICES='P'
    FINE_CHOICES='F'
    
    TRANSACTION_CHOICES=[
        ('P','Payment'),
        ('F','Fine'),
        
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES,blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} for {self.checkout}"





class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    reader=models.ForeignKey(Reader,on_delete=models.CASCADE)
    rating=models.IntegerField()