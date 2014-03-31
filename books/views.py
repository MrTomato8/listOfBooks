# -*- coding: utf-8 -*-
from django.contrib.comments import CommentForm
from django.http import Http404
from django.shortcuts import render, render_to_response
from forms import BooksForm
from models import Books
from django.template import RequestContext


def main(request):
    items = Books.objects.all()
    if request.method == "POST":
        form = BooksForm(request.POST or None)
        if form.is_valid() and request.is_ajax():
            form.save()
            return render(request, 'add_book.html', {'items': items, 'form': form},
                          context_instance=RequestContext(request))
    else:
        form = BooksForm()
    return render(request, 'main.html', {'items': items, 'form': form},
                      context_instance=RequestContext(request))


def detail(request, id):
    try:
        id = int(id)
        item = Books.objects.filter(pk=id)[0]
    except ValueError:
        raise Http404()
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid() and request.is_ajax():
            import time
            time.sleep(5)
            # response is just the form
            return render(request, 'add_comment.html', {'item': item, 'id': id}, context_instance=RequestContext(request))
    else:
        # response is the entire page
        return render(request, 'detail.html', {'item': item, 'id': id}, context_instance=RequestContext(request))


def search(request):
    return

