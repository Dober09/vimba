from unicodedata import category
from django.shortcuts import render
from .models import Categories

# Create your views here.
def article_page(request):
    cartegories = Categories.objects.all()
    context = {
        'cartegories':cartegories
    }
    return render(request,'articles/main_page.html',context)


def article_detail(request,slug):
    cartegory = Categories.objects.get(slug=slug)
    context = {
        'cartegory':cartegory
    }
    return render(request,'articles/details_page.html',context)