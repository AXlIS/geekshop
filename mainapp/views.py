from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, page=1, category_id=0):
    goods = Product.objects.filter(category_id=category_id).order_by(
        'price') if category_id > 0 else Product.objects.all().order_by('price')
    paginator = Paginator(goods, 3)

    # if request.user.is_authenticated:
    #     baskets = Basket.objects.filter(user=request.user)
    #     for basket in baskets:
    #         print(basket.product)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'GeekShop - Продукты',
        'catalog': ProductCategory.objects.all(),
        'products': products_paginator,
        'category_num': category_id
    }
    return render(request, 'mainapp/products.html', context)
