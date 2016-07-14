from __future__ import unicode_literals
from django.db import models
import datetime
# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):  # __unicode__ on Python 2 only but we have used here from __future__ import unicode_literals !
        return self.name

    class Meta:
        ordering = ['name']
        

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    def __str__(self):
        return u'%s %s' % (self.first_name,self.last_name)
  

class BookManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(title__icontains=keyword).count()        

class Book(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True,auto_now_add=True) #auto_now_add-- only on creation!
    objects = BookManager() #Remeber () after BookManager!Otherwise it will not work!

    def __str__(self):
        return self.title
