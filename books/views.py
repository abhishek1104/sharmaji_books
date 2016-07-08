from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from .models import Book
from .forms import ContactForm
from django.core.mail import send_mail
from django.core.urlresolvers import reverse #reverse to be used with HttpResponse !


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


def thanksji(request):
    return render(request,'books/thanks.html',{})

