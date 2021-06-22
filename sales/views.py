from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sales.models import Sale
from sales.forms import SalesSearchForm

# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)
    hello = 'hello world how are you'

    context = {
        'hello' : hello,
        'form':form,
    }

    return render(request, 'sales/home.html' , context)


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    # if template_name is not be specified then by default it will set model_detail.html

    # context_object_name = 'some name'
    # if the context name is not provided then b 

class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'


def sale_list_view(request):
    qs = Sale.objects.all()
    return render(request, 'sales/main.html', {'object_list':qs})


def sale_detail_view(request, pk):
    obj = Sale.objects.get(pk=pk)

    return render(request, 'sales/detail.html', {'object':obj})