from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=250,unique=True)
    cat_slug=models.SlugField(max_length=250,unique=True)
    cat_description=models.TextField(blank=True)
    cat_image=models.ImageField(upload_to='category',blank=True)
    class Meta:
        ordering=('cat_name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('shopcartapp:products_by_category',args=(self.cat_slug,))
    def __str__(self):
        return '{}'.format(self.cat_name)


class Product(models.Model):
    prod_name=models.CharField(max_length=250,unique=True)
    prod_slug=models.SlugField(max_length=250,unique=True)
    prod_description=models.TextField(blank=True)
    prod_price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    prod_image=models.ImageField(upload_to='product',blank=True)
    prod_stock=models.IntegerField()
    prod_available=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shopcartapp:prodCatDetails',args=[self.category.cat_slug,self.prod_slug,])
    class Meta:
        ordering=('prod_name',)
        verbose_name='product'
        verbose_name_plural='products'
    def __str__(self):
        return '{}'.format(self.prod_name)
