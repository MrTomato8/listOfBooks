from django.contrib.comments import CommentForm
from django.http import Http404
from django.shortcuts import render
from books.forms import BooksForm
from books.models import Books
from django.template import RequestContext


def main(request):
    items = Books.objects.all()
    form = BooksForm()
    if request.is_ajax():
        form = BooksForm(request)
        if form.is_valid():
            items = Books.objects.all()
            form.save()
            return render(request, 'add_book.html', {'items': items,
                                                     'form': form},
                          context_instance=RequestContext(request))
    else:
        return render(request, 'main.html', {'items': items, 'form': form},
                      context_instance=RequestContext(request))


def detail(request, id):
    try:
        id = int(id)
        item = Books.objects.filter(pk=id)[0]
    except ValueError:
        raise Http404()
    if request.method == "POST":
        form = CommentForm(request)
        if form.is_valid() and request.is_ajax():
            # import time
            # time.sleep(5)
            # response is just the form
            return render(request, 'add_comment.html', {'item': item, 'id': id}, context_instance=RequestContext(request))
    else:
        # response is the entire page
        return render(request, 'detail.html', {'item': item, 'id': id}, context_instance=RequestContext(request))

