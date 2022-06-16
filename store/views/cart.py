from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import  Product

class Cart(View):
    def get(self , request):
        print(request.session.get('cart').keys())
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        # products['stripe_publishable_key']=settings.STRIPE_PUBLIC_KEY
        print(products)
        return render(request , 'cart.html' , {'products' : products})

# from django.views.generic import ListView, CreateView, DetailView, TemplateView
# class Cart(DetailView):
#     model = Product
#     template_name = "cart.html"
#     pk_url_kwarg = 'id'

#     '''
#     Here in this code, we are overriding the get_context_data() method to add publishable key as a data to the template context.
#     We set pk_url_kwarg = 'id' to instruct Django to fetch details of the product with the id passed as a URL parameter.
#     '''
    
#     def get_context_data(self, **kwargs):
#         context = super(Cart, self).get_context_data(**kwargs)
#         print(context)
#         context['stripe_publishable_key'] = settings.STRIPE_PUBLIC_KEY
#         print(context)
#         return context  


from django.conf import settings
from django.http.response import HttpResponseNotFound, JsonResponse
from store.models.orders import Order
import json
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_checkout_session(request, id):
    
    print(id)
    request_data = json.loads(request.body)
    customer_email = request_data['email']
    print(customer_email)
    customer=Customer.objects.filter(email=customer_email)
    
    print('_______________')
    # print(request_data)
    product = get_object_or_404(Product, pk=id)
    # print(product)

    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_session = stripe.checkout.Session.create(
        # Customer Email is optional,
        # It is not safe to accept email directly from the client side
        customer_email = request_data['email'],
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                    'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(reverse('failed')),
    )

    # OrderDetail.objects.create(
    #     customer_email=email,
    #     product=product, ......
    # )

    order = Order()
    # order.customer.email = request_data['email']
    order.product = product
    order.customer=customer[0]
    order.stripe_payment_intent = checkout_session['payment_intent']
    order.price = int(product.price * 100)
    order.save()

    # return JsonResponse({'data': checkout_session})
    return JsonResponse({'sessionId': checkout_session.id})

from django.views.generic import ListView, CreateView, DetailView, TemplateView
class PaymentSuccessView(TemplateView):
    template_name = "payment_success.html"

    def get(self, request, *args, **kwargs):
        session_id = request.GET.get('session_id')
        print(session_id)
        if session_id is None:
            return HttpResponseNotFound()
        
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # print(stripe.api_key)
        session = stripe.checkout.Session.retrieve(session_id)
        # print(session)

        order = get_object_or_404(Order, stripe_payment_intent=session.payment_intent)
        # order.has_paid = True
        order.save()
        return render(request, self.template_name)

class PaymentFailedView(TemplateView):
    template_name = "payment_failed.html"




 