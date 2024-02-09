from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category, Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict= {}
    #creates a context dictionary for data to be passed into template
    context_dict['boldmessage']= 'Crunchy, creamy, cookie, candy, cupcake!'
    #this passes the key 'boldmessage' into index.html's {{ bold_message }}
    context_dict['categories']= category_list
    #passing the var set in category list by mapping it to key within context dict
    return render(request, 'rango/index.html', context= context_dict)
    #return the template response

def about(request):
    context_dict= {'boldmessage': 'This tutorial has been put together by Jack B',
                   'MEDIA_URL': '/media/cat.jpg'}
    return render(request, 'rango/about.html', context= context_dict)
    #return the template response
