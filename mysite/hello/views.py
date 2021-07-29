from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    num_visit = request.session.get('num_visit',0)+1
    request.session['num_visit'] = num_visit
    if num_visit >4:
        del(request.session['num_visit'])
    resp = HttpResponse('view count=' +str(num_visit))
    resp.set_cookie('dj4e_cookie', 'e46709aa', max_age=1000)
    return resp




