from django.shortcuts import render
from books.models import Book
from datetime import date


def books_view(request, p_date=None):
    template = 'books/books_list.html'

    try:
        year, month, day = [int(x) for x in p_date.split('-')]
        p_date = date(year, month, day)
        print(p_date)
    except:
        p_date = None
    page, dates = None, None
    prev, next = '', ''
    if p_date:
        books_objects = Book.objects.filter(pub_date=p_date)
        dates = sorted(
            [el.pub_date for el in Book.objects.all()], reverse=True)
        data_index = dates.index(p_date)
        prev = str(dates[data_index-1]) if data_index > 0 else ''
        next = str(dates[data_index-1]) if data_index < len(dates)-1 else ''
    else:
        books_objects = Book.objects.all()

    books = [{'name': book.name, 'author': book.author,
              'pub_date': book.pub_date} for book in books_objects]

    context = {
        'books': books,
        'prev': prev,
        'next': next

    }
    return render(request, template, context)
