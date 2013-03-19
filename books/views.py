from annoying.decorators import render_to
from django.http import Http404
from django.shortcuts import render
from books.models import Books
from django.template import RequestContext


@render_to('main.html')
def main(request):
    items = Books.objects.all()
    return {'items': items}


def detail(request, id):
    try:
        id = int(id)
        item = Books.objects.filter(pk=id)[0]
    except ValueError:
        raise Http404()
    if request.is_ajax():
        import time
        time.sleep(5)
        # response is just the form
        return render(request, 'add.html', {'item': item, 'id': id}, context_instance=RequestContext(request))
    else:
        # response is the entire page
        return render(request, 'detail.html', {'item': item, 'id': id}, context_instance=RequestContext(request))
