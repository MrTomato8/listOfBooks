# -*- coding: utf-8 -*-
from django.contrib.comments import CommentForm
from django.http import Http404
from django.shortcuts import render, render_to_response
from forms import BooksForm
from models import Books
from django.template import RequestContext


def main(request):
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid() and request.is_ajax():
            try:
                form.save()
            except:
                print "Ошибка сохранения!"
            items = Books.objects.all()
            return render_to_response('add_book.html', {'items': items, 'form': form},
                          RequestContext(request))
    else:
        items = Books.objects.all()
        form = BooksForm()
        return render_to_response('main.html', {'items': items, 'form': form},
                      RequestContext(request))


def detail(request, id):
    try:
        id = int(id)
        item = Books.objects.filter(pk=id)[0]
    except ValueError:
        raise Http404()
    if request.method == "POST":
        form = CommentForm(request)
        if form.is_valid() and request.is_ajax():
            import time
            time.sleep(5)
            # response is just the form
            return render(request, 'add_comment.html', {'item': item, 'id': id}, context_instance=RequestContext(request))
    else:
        # response is the entire page
        return render(request, 'detail.html', {'item': item, 'id': id}, context_instance=RequestContext(request))

