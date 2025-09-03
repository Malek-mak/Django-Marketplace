from django.shortcuts import render, redirect
from django.http import request
from django.urls import reverse
import paypalrestsdk
from django.conf import settings
from Users.models import CartModel

paypalrestsdk.configure({
    "mode": "live",  # Change to "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET,
})


def create_payment(request, id):
    amount = CartModel.objects.get(id=id)
    amount = amount.total_amount
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal",
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
        },
        "transactions": [
            {
                "amount": {
                    "total": amount,  # Total amount in USD
                    "currency": "USD",
                },
                "description": "Payment for Product",
            }
        ],
    })

    if payment.create():
        return redirect(payment.links[1].href)  # Redirect to PayPal for payment
    else:
        return render(request, 'payment/payment_failed.html')

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'payment/payment_success.html')
    else:
        return render(request, 'payment/payment_failed.html')



def payment_failed(request):
    return render(request, 'payment/payment_failed.html')