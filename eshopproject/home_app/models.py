from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.

# category table
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True,db_index=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='category')

    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_url(self):
        return reverse('pr_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)



# PRODUCT TABLE
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=True,null=False)
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='products')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()

    # def get_url(self):
    #     return reverse('pr_cat', args=[self.category])



    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        ordering=('-name',)

