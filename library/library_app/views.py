from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Shelf, Book, Hall

def index(request):
    shelfs = Shelf.objects.all()
    books = Book.objects.all()
    halls = Hall.objects.all()
    return render(request, "library_app/index.html", {'halls': halls, 'books': books, 'shelfs': shelfs})

def index_2(request):
    shelfs = Shelf.objects.all()
    books = Book.objects.all()
    halls = Hall.objects.all()
    return render(request, "library_app/index_2.html", {'halls': halls, 'books': books, 'shelfs': shelfs})