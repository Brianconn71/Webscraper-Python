from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def scrape(request):
    page = requests.get('https://www.facebook.com')
    soup = BeautifulSoup(page.text, 'html.parser')
    
    link_address = []
    
    for x in soup.find_all('a'):
        link_address.append(x.get('href'))
    
    template = 'base/result.html'
    context = {
        'link_address': link_address
    }
    
    return render(request, template, context)
