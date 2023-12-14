from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from products.models import Product, Basket
from users.models import User
from .forms import ProductForm
# Create your views here.
def index(request):
    context = {'title': 'Книжный сайт',}
    return render(request,'products/index.html',context)


def products(request):
    context={
        'title': 'Новинки',
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html',context)

def add(request):

    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error='Данные не верные'


    form = ProductForm()

    data = {
        'form': form,
        'error': error
    }
    context = {'title': 'Книжный сайт',}
    return render(request,'products/add.html',data)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
