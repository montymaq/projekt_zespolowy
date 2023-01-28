from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True) #do utworzeania adresu URL
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True) #opis produktu
    price = models.DecimalField(max_digits=10, decimal_places=2) #cena
    available = models.BooleanField(default=True) #dostępność
    created = models.DateTimeField(auto_now_add=True) #data i godzina utworzenia obiektu
    updated = models.DateTimeField(auto_now=True) # data modyfiakcji obiektu
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

class Meta:
    ordering = ('name',)
    index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name