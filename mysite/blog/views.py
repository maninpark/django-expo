from django.shortcuts import render

from django.http import HttpResponse
from .models import Post

# Create your views here.

def Hello(request):
    return HttpResponse('Hello world- welcome to my new blog')


#def TestHello(request):
#    f = open('/home/manin/Desktop/django expo/mysite/blog/templates/test.html')
#    content = f.read()
#    return HttpResponse(content)

#def TestHello(request):
#    context = {'blogdb':[{'title':'my first blog -manindra','content':'Hey there i am learning deploying the admin - manindra'},{'title':'my first blog -anu','content':'Hey there i am learning deploying the admin - anu'}]}

#    return render(request,'test.html',context)





def TestHello(request):
    context = {'blogdb':Post.objects.all()}
    print context

    return render(request,'test.html',context)