from annoying.decorators import render_to
from django.http import Http404
from books.models import Books


@render_to('main.html')
def main(request):
    items = Books.objects.all()
    return {'items' : items}

@render_to('detail.html')
def detail(request,id):
    try:
        id = int(id)
        item = Books.objects.filter(pk=id)[0]
    except ValueError:
        raise Http404()
    return {'form' : item}
