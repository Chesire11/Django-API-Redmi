from django.db import models

# Create your models here.
from django.db import models

class Redmi(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='redmi/')

    def __str__(self):
        return self.name

class RedmiVariant(models.Model):
    redmi = models.ForeignKey(Redmi, related_name='variants', on_delete=models.CASCADE)
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()

    def __str__(self):
        return f"{self.redmi.name} - {self.name}"
