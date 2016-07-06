from django.shortcuts import render
from django.http import Http404,HttpResponse
from .models import Book
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
            return render(request,'search_results.html',{'books':books,'query':q})
    return render(request,'search_form.html',{'error':error})