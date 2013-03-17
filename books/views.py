from annoying.decorators import render_to
from django.http import Http404
from django.shortcuts import render_to_response
from books.models import Books
from django.template import RequestContext


@render_to('main.html')
def main(request):
    items = Books.objects.all()
    return {'items' : items}

def detail(request,id):
    try:
        id = int(id)
        item = Books.objects.filter(pk=id)[0]
    except ValueError:
        raise Http404()
    return render_to_response('detail.html', {'item' : item, 'id' : id,},
                                context_instance=RequestContext(request))

