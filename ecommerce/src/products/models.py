from django.db import models
from django.db.models.signals import pre_save,post_save
# Create your models here.
# from .utils import unique_slug_generator
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=20 ,default=5.99)
    slug=models.SlugField(default='pro',blank=True,unique=True)
    featured=models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator

pre_save.connect(product_pre_save_receiver,sender=Product)