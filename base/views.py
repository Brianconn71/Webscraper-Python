from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link

# Create your views here.

def scrape(request):
    page = requests.get('https://www.google.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    for x in soup.find_all('a'):
        link_address = x.get('href')
        link_text = x.string
        Link.objects.create(address=link_address, name=link_text)
    
    data = Link.objects.all()
    
    template = 'base/result.html'
    context = {
        'data': data,
    }
    
    return render(request, template, context)
