from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict= {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #this passes the key 'bold_message' into index.html's {{ bold_message }}
    return render(request, 'rango/index.html', context= context_dict)
    #return the template response

def about(request):
    context_dict= {'boldmessage': 'This tutorial has been put together by Jack B',
                   'MEDIA_URL': '/media/cat.jpg'}
    return render(request, 'rango/about.html', context= context_dict)
    #return the template response
