from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
#from django.db import connection
# Create your models here.


def dictfetchall(cursor):
    "Returns all rows in form of dictionary"
    desc=cursor.description
    return [
    dict(zip([col[0] for col in desc],row))
        for row in cursor.fetchall()
    ]


@python_2_unicode_compatible
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
    

@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    last_accessed = models.DateTimeField()
    def __str__(self):
        return '%s %s' % (self.first_name,self.last_name)
  


class BookManager(models.Manager): # Not write @python_2_unicode_compatible as only define where __str__ is placed!
    def title_count(self,keyword):
        return self.filter(title__icontains=keyword).count()  


class KapilBookManager(models.Manager):
    def get_queryset(self):
        return super(KapilBookManager,self).get_queryset().filter(authors__first_name__icontains='kapil') 


@python_2_unicode_compatible
class Book(models.Model):
    title = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author, db_table='book_author_rel')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True,auto_now_add=True) #auto_now_add-- only on creation!
    #objects = BookManager() #Remeber () after BookManager!Otherwise it will not work!
    objects=BookManager() # Use objects=models.Manager() otherwise!
    kapil_objects=KapilBookManager()

    class Meta:
        db_table='book'

    def __str__(self):
        return self.title

class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager,self).get_queryset().filter(sex='M')


class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager,self).get_queryset().filter(sex='F')


@python_2_unicode_compatible
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
        return '{0} {1} is the person'.format(self.first_name,self.last_name,)


    full_name = property(_get_full_name)

    def __str__(self):
        return self.full_name


class PollManager(models.Manager): #write this above classs OpinionPoll otherwise it won't work!
    def with_counts(self):
        from django.db import connection
        cursor=connection.cursor()
        cursor.execute("""SELECT p.id, p.question, p.poll_date, COUNT(*)
            FROM opinionpoll p, response r
            WHERE p.id = r.poll_id
            GROUP BY p.id, p.question, p.poll_date
            ORDER BY p.poll_date DESC """)

        result_list=[]

        for row in cursor.fetchall():
            p=self.model(id=row[0],question=row[1],poll_date=row[2])
            p.num_response=row[3]
            result_list.append(p)

        return result_list



@python_2_unicode_compatible #We must define __str__ method in the model (here OpinionPoll) otherwise it will throw error
class OpinionPoll(models.Model):
    question=models.CharField(max_length=50)
    poll_date=models.DateField()


    class Meta:
        db_table='opinionpoll' #We need to write custom table name within quotes.

    def __str__(self): 
        return self.question #use return otherwise it will show error coersion to unicode!
    objects=PollManager()


@python_2_unicode_compatible
class Response(models.Model):
    poll=models.ForeignKey(OpinionPoll,verbose_name="the related poll",related_name='poll') 
    person_name=models.CharField(max_length=50)


    class Meta:
        db_table='response' #We need to write custom table name within quotes.

    def __str__(self): 
        return self.person_name



