from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):    
    title=models.CharField(max_length=50,null=True)  

    def __str__(self):
        return self.title
        
class Post(models.Model):
    
    title=models.CharField(max_length=100, verbose_name='Başlık')
    content=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Kategori',null=True)
    createDate=models.DateTimeField(auto_now_add=True)
    img=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.title

