from django.shortcuts import render
from mainapp.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Продукты',
        'catalog': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'добро подаловать!',
        'username': 'Igor Svistun',
        'products': [
            {'name': 'Черное худи', 'price': '2 990 руб.'},
            {'name': 'Джинсы', 'price': '5 800 руб.'}
        ],
        'promotion': True,
        'promotion_products': [
            {'name': 'Туфли Dr.Martens', 'price': '10 000 руб.'}
        ],
    }
    return render(request, 'mainapp/context.html', context)
