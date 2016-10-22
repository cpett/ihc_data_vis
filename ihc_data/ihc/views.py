from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    '''
        Loads the index/home page
    '''
    return render(request, 'index.html')


def dashboard(request):
    '''
        Loads the page with all the Tableau things
    '''
    return render(request, 'dashboard.html')
