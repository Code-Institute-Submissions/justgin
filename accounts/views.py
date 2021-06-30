from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserAccount
from .forms import UserAccountForm

from checkout.models import Order


def account(request):
    """ Display users account. """
    account = get_object_or_404(
        UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(
            request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your account has been updated.')

    form = UserAccountForm(instance=account)
    orders = account.orders.all()

    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
        'on_account_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(
        Order, order_number=order_number)

    messages.info(
        request, (
            f'These are the details of a past Gin purchase, order number: {order_number}. We sent an email to let you know, at the time.'
        )
    )

    template = 'checkout/checkout_succ.html'
    context = {
        'order': order,
        'from_account': True,
    }

    return render(request, template, context)
