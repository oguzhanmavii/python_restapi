from django.db import models

class Product(models.Model):
    productId=models.AutoField(primary_key=True)
    productName=models.CharField(max_length=50)
    productPrice=models.DecimalField(max_digits=10,decimal_places=2)
    productQuantity=models.IntegerField()
    
    def __str__(self) -> str:
        return self.productName