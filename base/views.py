from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link

# Create your views here.

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
    
        for x in soup.find_all('a'):
            link_address = x.get('href')
            link_text = x.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    template = 'base/result.html'
    context = {
        'data': data,
    }
    
    return render(request, template, context)


def clear(request):
    Link.objects.all().delete()
    
    template = 'base/result.html'
    
    return render(request, template)
