from django.shortcuts import render
from django.db import connection

# Create your views here.

def get_cursor():
    return connection.cursor()

def index(request):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book")
    books = cursor.fetchall()
    # books is a list of tuples
    # [(1,sanguo,luoguanzhong)]

    # return result to template
    return render(request,'index.html',context={"books":books})

def add_book(request):
    pass

def book_detail(request,book_id):
    pass

