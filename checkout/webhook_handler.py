from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product
from accounts.models import UserAccount

import json
import time


class StripeWH_Handler:
    """Intercepts webhooks from Stripe"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Deals with all unknown/unexpected webhook events.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Deals with Stripe's payment_intent.succeeded webhook.
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Data included in Delivery Details.
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Updates account details if save_info box was ticked.
        account = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            account = UserAccount.objects.get(user__username=username)
            if save_info:
                account.default_phone_number = shipping_details.phone
                account.default_country = shipping_details.address.country
                account.default_postcode = shipping_details.address.postal_code
                account.default_town_or_city = shipping_details.address.city
                account.default_street_address1 = shipping_details.address.line1
                account.default_street_address2 = shipping_details.address.line2
                account.default_county = shipping_details.address.state
                account.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_account=account,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order within webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Deals with Stripe's payment_intent.payment_failed webhook.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
