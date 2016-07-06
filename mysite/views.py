from django.http import Http404,HttpResponse
import datetime
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world")


def current_Datetimereq(request):
    now=datetime.datetime.now()
    '''
    html="""<html>It is now {0}""".format(now,)
    return HttpResponse(html)
    '''
    return render(request,'current_Datetime.html',{'current_date':now})


def hours_ahead(request,offset):
    try:
        offset = int(offset) #offset would be a unicode string from url.We need to do it  for tn variable value assignment!
    except ValueError : 
        raise Http404()
    tn = datetime.datetime.now()+datetime.timedelta(hours=offset)
    '''
    assert False #Trigger the error page
    html = """In {0} hour(s),it will be {1}""".format(offset,tn,)
    return HttpResponse(html)
    '''
    return render(request,'hours_ahead.html',{'hours_offset':offset,'future_time':tn})

