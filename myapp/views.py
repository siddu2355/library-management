from django.shortcuts import render
from rest_framework import viewsets
from .models import Author, Book, Borrower, Transaction, Fine
from .serializers import AuthorSerializer, BookSerializer, BorrowerSerializer, TransactionSerializer, FineSerializer


def home(request):
    return render(request, 'home.html')

def customers(request):
    return render(request, 'customers.html')

def authors(request):
    return render(request, 'authors.html')

def books(request):
    return render(request, 'books.html')

def fines(request):
    return render(request, 'fines.html')

def transactions(request):
    return render(request, 'transactions.html')

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
