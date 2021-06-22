from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from mainapp.models import Product
from basketapp.models import Basket


# Create your views here.
@login_required
def basket_add(request, product_id=None):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    if request.is_ajax():
        Basket.objects.get(id=id).delete()
        return JsonResponse({'result': render_to_string('basketapp/basket.html')})


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
        # baskets = Basket.objects.filter(user=request.user)
        # context = {'baskets': baskets}
        return JsonResponse({'result': render_to_string('basketapp/basket.html')})
