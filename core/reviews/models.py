from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_img/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    variation = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(upload_to='products_img/', blank=True, null=True)
  
    def __str__(self) -> str:
        return f'{self.name} - {self.brand}'
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(validators=[ 
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    comment = models.TextField(max_length=1000)
    posted_on = models.DateTimeField(default=timezone.now)
    dupes = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.product.name}'