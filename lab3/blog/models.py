from django.db import models

from django.contrib import admin

# Create your models here.

class Author(models.Model):
    AuthorID = models.CharField(max_length = 150)
    Name = models.CharField(max_length = 150)
    Age = models.IntegerField(max_length = 150)
    Country = models.CharField(max_length = 150)

class Book(models.Model):
    ISBN = models.CharField(max_length = 150)
    Title = models.CharField(max_length = 150)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 150)
    PublishDate = models.DateField()
    Price = models.FloatField(max_length = 150)


admin.site.register(Author)
admin.site.register(Book)

def __unicode__(self):
    return self.AuthorID 