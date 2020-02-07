from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Categories(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Blog(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=RichTextField(blank=True, null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics',default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.content[:100]+"..."

