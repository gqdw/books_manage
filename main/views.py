from django.shortcuts import render
from django.http import HttpResponse
from main.models import Book
# Create your views here.

def Index(request):
	return HttpResponse('ok')

def booklist(request):
	books = Book.objects.all()
	return render(request, 'booklist.html', {'books':books})
