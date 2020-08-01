from django.shortcuts import render, get_object_or_404
from .models import Place

def test2(requests):
    return render(requests, 'test2.html')

def list(request):
    places = Place.objects
    return render(request, 'list.html', {'places':places})
    
def test3(requests):
    places = Place.objects
    return render(requests, 'test3.html', {'places':places})

def detail2(request, image_id):
    details = get_object_or_404(Place, pk = image_id)
    return render(request, 'detail.html', {'detail':details})
  
def main(request):
    return render(request, 'main.html')

def main2(request):
    return render(request, '2번째.html')

def detail(request):
    return render(request, 'detail.html')

def about(request):
    return render(request, 'about.html')

