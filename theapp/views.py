from django.shortcuts import render, get_object_or_404
from .models import Place

def test(requests):
    places = Place.objects
    return render(requests, 'test.html', {'places':places})

def test2(requests):
    return render(requests, 'test2.html')

def detail(request, image_id):
    details = get_object_or_404(Place, pk = image_id)
    return render(request, 'detail.html', {'detail':details})