from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Items



# Define the home view
def home(request):
    items = Items.objects.all()
    return render(request, 'home.html', {
      'items': items
    })

class ItemCreate(CreateView):
    model = Items
    fields = "__all__"
    success_url = '/'

class ItemDelete(DeleteView):
    model = Items
    success_url = '/'