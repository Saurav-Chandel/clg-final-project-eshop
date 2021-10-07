from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.item import Item

from django.views import View
from math import ceil


def carousel(request):
    products = Item.objects.all()
    print(products)
    n=len(products)
    nslides = n//4+ceil((n/4)-(n//4))
    # a=Product.objects.get(product_name='dress')
    # print(a.image)
    params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    return render(request,'index.html',params)