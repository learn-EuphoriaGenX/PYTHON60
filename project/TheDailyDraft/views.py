from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import razorpay
from BlogDrafts.models import Payment
from UserAuth.models import PremiumUser

# Razorpay client
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
)

# 🔐 Secure Plan Mapping (NO FRONTEND PRICE TRUST)
PLAN_PRICES = {
    'Starter': 99,
    'Pro': 199,
    'Premium': 299
}


def MyHome(req):
    return render(req, 'home.html')


@login_required(login_url='login')
def Pricing(req):
    if req.method == 'POST' and 'select_plan' in req.POST:

        plan = req.POST.get('plan_name')

        # 🔴 Prevent tampering
        if plan not in PLAN_PRICES:
            return render(req, 'failed.html', {'message': 'Invalid Plan Selected'})

        amount = PLAN_PRICES[plan] * 100  # in paise
        currency = 'INR'
        user = req.user

        # Create Razorpay order
        razorpay_order = razorpay_client.order.create({
            'amount': amount,
            'currency': currency,
            'payment_capture': '1'
        })

        # Save in DB
        Payment.objects.create(
            user=user,
            amount=amount,
            razorpay_order_id=razorpay_order['id'],
            status='Created'
        )

        context = {
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_merchant_key': settings.RAZOR_KEY_ID,
            'razorpay_amount': amount,
            'display_amount': amount / 100,
            'currency': currency,
            'callback_url': 'http://127.0.0.1:8000/paymenthandler/',
            'user_name': user.username,
            'user_email': user.email,
            'plan_name' : plan,
        }

        return render(req, 'payment.html', context)

    # Plans UI
    plans = [
        {'name': 'Starter', 'price': '99'},
        {'name': 'Pro', 'price': '199'},
        {'name': 'Premium', 'price': '299'}
    ]

    return render(req, 'pricing.html', {'plans': plans})


# ✅ Payment Handler
@csrf_exempt
def paymenthandler(req):
    if req.method == "POST":

        payment_id = req.POST.get('razorpay_payment_id')
        order_id = req.POST.get('razorpay_order_id')
        signature = req.POST.get('razorpay_signature')

        try:
            # Verify signature
            razorpay_client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })

            payment = Payment.objects.get(razorpay_order_id=order_id)

            # ❌ DO NOT CAPTURE AGAIN (already auto-captured)
            # razorpay_client.payment.capture(payment_id, payment.amount)

            # Update DB
            payment.razorpay_payment_id = payment_id
            payment.razorpay_signature = signature
            payment.status = 'Success'
            payment.save()

            # 🎯 Upgrade User
            pre_user = PremiumUser.objects.filter(user=payment.user)
            pre_user.update(is_premium=True)

            messages.success(req, 'Payment successful')
            context = {
                'message' : "Payment Successful",
                'order_id' : payment.razorpay_order_id,
                'amount' : payment.amount / 100,
                'plan' : req.POST.get('plan_name'),
                
            }
            return render(req, 'success.html', context)

        except Exception as e:
            print("Payment Error:", e)

            return render(req, 'failed.html', {
                'message': 'Payment verification failed'
            })

    return render(req, 'failed.html', {'message': 'Invalid request'})