from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict= {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #this passes the key 'bold_message' into index.html's {{ bold_message }}
    return render(request, 'rango/index.html', context= context_dict)
    #return the template response

def about(request):
    #our link from about to index with pathing
    return HttpResponse("Rango says here is the about page. <a href= '/rango/'>Index</a>")
