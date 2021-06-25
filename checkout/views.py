from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's no Gin in your Cart!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,

    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Deals with successful orders.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    profile = UserProfile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()

    messages.success(request, f'Processed your purchase. Let the Gin flow. \
        The order number is: {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_succ.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
