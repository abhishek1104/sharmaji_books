from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .models import Book,Publisher,Author
from .forms import ContactForm
from django.core.mail import send_mail
from django.core.urlresolvers import reverse #reverse to be used with HttpResponse !
from django.views.generic import ListView,DetailView
from django.utils import timezone

# Create your views here.


#def search_form(request):
#    return render(request,'search_form.html')

def search(request):
    '''
    if 'q' in request.GET:
        message="You are searching for %r" % request.GET['q'] #%r converts it using repr() and %s to string!
    else:
        message="You submitted an empty form."
    return HttpResponse(message)
    '''
    '''
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        books=Book.objects.filter(title__icontains=q)
        return render(request,'search_results.html',{'books':books,'query':q})
    else:
        #return HttpResponse('Please Submit a search item.')
        return render(request,'search_form.html',{'error':True})
    '''

    error=[]

    if 'q' in request.GET:
        q=request.GET['q']

        if not q:
            error.append("Enter a search term.")
        elif len(q)>10:
            error.append("Enter atmost 10 charatctes.")
        else:
            books=Book.objects.filter(title__icontains=q)
            return render(request,'books/search_results.html',{'books':books,'query':q})
    return render(request,'books/search_form.html',{'error':error})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(cd['subject'],cd['message'],cd.get('email','noreply@example.com'),
                ['abhishek1104@gmail.com'],
            )

            return HttpResponseRedirect(reverse('myapp:thanksbaboo')) #reverse for url redirect! #app_name:name(urlname)
            #Note here it is <namespace i.e. name under main settings url>:<name under books.url i.e. for desired url>
    else :
        form= ContactForm(initial={'subject':'I love my site','email':'abhishek.sharma@pulpstrategy.com'})

    return render(request,'books/contact_form_custom.html',{'form':form})


def thanksji(request,waooo='000waooo00uuuu'):
    return render(request,'books/thanks.html',{'somevariable':waooo})


'''
class PublisherList(ListView):
    model=Publisher
'''

class PublisherList(ListView):
    model=Publisher

    def get_context_data(self,**kargs):
        context=super(PublisherList,self).get_context_data(**kargs)
        context['book_list'] = Book.objects.all()

        return context

class PublisherList1(ListView):
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()
    template_name = 'books/publisher_list.html'

    '''def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher)'''


class PublisherList2(ListView):

    template_name = 'books/publisher_list2.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.args[0])
        return Book.objects.filter(publisher=self.publisher) #It returns context_object_name by default would be book_list if not mentioned!


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherList2, self).get_context_data(**kwargs)
        # Add in the publisher
        context['who_publisher'] = self.publisher        
        return context


class AuthorDetailView(DetailView):
    queryset=Author.objects.all() 

    def get_object(self):

        #call superclass
        object=super(AuthorDetailView,self).get_object()
        #Record the last accessed time
        object.last_accessed = timezone.now()
        object.save()
        #Return the object
        return object