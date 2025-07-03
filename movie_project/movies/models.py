from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Cast(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BaseContent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    categories = models.ManyToManyField(Category)
    casts = models.ManyToManyField(Cast)
    poster_image = models.ImageField(upload_to='posters/')
    class Meta:
        abstract = True

class Movie(BaseContent):
    pass

class Series(BaseContent):
    pass