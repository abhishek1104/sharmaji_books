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


class KapilBookManager(models.Manager):
    def get_queryset(self):
        return super(KapilBookManager,self).get_queryset().filter(authors__first_name__icontains='kapil')      

class Book(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True,auto_now_add=True) #auto_now_add-- only on creation!
    #objects = BookManager() #Remeber () after BookManager!Otherwise it will not work!
    objects=BookManager() # Use objects=models.Manager() otherwise!
    kapil_objects=KapilBookManager()

    def __str__(self):
        return self.title


class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager,self).get_queryset().filter(sex='M')

class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager,self).get_queryset().filter(sex='F')

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1,choices=(('M','Male'),('F','Female'),))
    birth_date = models.DateField()
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()

    '''
    def __str__(self):
        return u'{0} {1} is the person'.format(self.first_name,self.last_name,)
    '''
    def when_born(self):
        import datetime

        if self.birth_date <= datetime.date(1990,01,01):
            return "Older"
        else:
            return "Younger"

    def _get_full_name(self):
        return u'{0} {1} is the person'.format(self.first_name,self.last_name,)


    full_name = property(_get_full_name)

