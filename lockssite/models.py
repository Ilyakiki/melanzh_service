from django.db import models
from django.core.validators import MinValueValidator

class Service(models.Model):
    #Модель предоставляемых услуг
    description=models.CharField(max_length=300)
    price=models.IntegerField(validators=[MinValueValidator(0)],null=True,default=None)

    def __str__(self):
        return f'{self.description} {self.price}'
