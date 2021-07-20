from django.conf import settings
from django.core.cache import cache
import os
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from mainapp.models import ProductCategory, Product


def get_categories():
    if settings.LOW_CACHE:
        key = 'menu_categories'
        menu_categories = cache.get(key)
        if menu_categories is None:
            menu_categories = ProductCategory.objects.all()
            cache.set(key, menu_categories)
        return menu_categories
    else:
        return ProductCategory.objects.all()


def index(request):
    context = {'title': 'Geekshop'}
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None, page=1):
    prod_list = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(prod_list, per_page=3)
    try:
        prod_paginator = paginator.page(page)
    except PageNotAnInteger:
        prod_paginator = paginator.page(page=1)
    except EmptyPage:
        prod_paginator = paginator.page(paginator.num_pages)
    context = {'title': 'Geekshop - Каталог',
               'product_list': prod_paginator,
               'categories': get_categories()}
    return render(request, 'mainapp/products.html', context)

