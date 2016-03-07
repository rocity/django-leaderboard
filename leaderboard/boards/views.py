from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Item


# Create your views here.
def index(r):
    items = Item.objects.all()
    context = {
        'item_list': items
    }

    return render(r, 'boards/index.html', context)


def detail(r, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(r, 'boards/details.html', {'item': item})


def vote(r, item_id):
    return HttpResponse("Voting on item %s" % item_id)
