from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Item


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'boards/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.order_by('-score')


class DetailView(generic.DetailView):
    model = Item
    template_name = 'boards/details.html'


def vote(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    item.score += 1
    item.save()
    return HttpResponseRedirect(reverse('boards:index'))
