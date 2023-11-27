from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default="", null=False, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"

class Course(models.Model):
    title = models.CharField(max_length= 50)
    subtitle = models.CharField(max_length= 100, default="")
    description = RichTextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="", blank=True, null= False, unique=True, db_index=True)
    # Foreign Key ile Many to One bağlantısı sağlandı
    category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(args,kwargs)

    def __str__(self):
        return f"{self.title}"