import requests
from bs4 import BeautifulSoup

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Link


# Create your views here.
def scrape(request):

  if 'POST' == request.method:
    site_address = request.POST.get('url', '')

    page = requests.get(site_address)

    soup = BeautifulSoup(page.text, 'html.parser')

    for link in soup.find_all('a'):
      
      url = link.get('href')
      name = link.string

      Link.objects.create(name = name, url = url)
    
    return HttpResponseRedirect('/')
  else:
    data = Link.objects.all()
  
  return render(request, 'myapp/result.html', { 'links': data })


def clear(request):
  
  Link.objects.all().delete()

  return render(request, 'myapp/result.html')
