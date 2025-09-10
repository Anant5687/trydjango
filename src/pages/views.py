from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request, args, kwargs)
    my_context = {
        'my_text': "This is all about home page",
        'my_number':8327498,
        'my_list': [123, 321, 213, 32, 31]
    }
    # return HttpResponse("<h1>Hello world!</h1>")
    return render(request, 'home.html', my_context)

def contact_view (request,*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")