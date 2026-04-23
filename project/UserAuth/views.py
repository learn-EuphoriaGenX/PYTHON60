from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import OtpModel, PremiumUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import random
import re
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('useremail')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, 'All fields are required')
            return redirect('register')

        
        alreadyExists = User.objects.filter(username=username).exists()

        if alreadyExists:
            messages.error(request, 'Username already exists')
            return render(request, 'register.html')
        
        alreadyExists = User.objects.filter(email=email).exists()
        if alreadyExists:
            messages.error(request, 'Email already exists')
            return render(request, 'register.html')
        
        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            PremiumUser.objects.create(user=new_user, is_premium=False)
            messages.success(request, 'User registered successfully')
            return render(request, 'login.html')

    return render(request, 'register.html')

def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return messages.error(request, 'All fields are required')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

def Logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')


from django.utils import timezone
from datetime import timedelta

def ForgetPassword(request):
    if request.method == 'POST' and 'send_otp' in request.POST:
        username_or_email = request.POST.get('username_or_email')

        if not username_or_email:
            messages.error(request, 'Please enter username or email')
            return redirect('forget-password')

        user = None
        if '@' in username_or_email:
            user = User.objects.filter(email=username_or_email).first()
        else:
            user = User.objects.filter(username=username_or_email).first()

        if not user:
            messages.error(request, 'User not found')
            return redirect('forget-password')

        OtpModel.objects.filter(user=user).delete()

        otp = random.randint(1000, 9999)
        OtpModel.objects.create(
            user=user,
            otp=otp,
            created_at=timezone.now()
        )
    
        try:
            send_mail(
                'Password Reset OTP',
                f'Your OTP is {otp}. Valid for 10 minutes.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
        except Exception as e:
            messages.error(request, 'Failed to send email')
            return redirect('forget-password')

        messages.success(request, f'OTP {otp} sent to {user.email}')
        return render(request, 'submit-otp.html', {'username': user.username})

    if request.method == 'POST' and 'resend_otp' in request.POST:
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()
      

        if not user:
            return redirect('forget-password')

        OtpModel.objects.filter(user=user).delete()

        otp = random.randint(1000, 9999)
        OtpModel.objects.create(user=user, otp=otp, created_at=timezone.now())

        send_mail(
            'Password Reset OTP',
            f'Your OTP is {otp}. Valid for 10 minutes.',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )

        messages.success(request, f'New OTP {otp} sent to {user.email}')
        return render(request, 'submit-otp.html', {'username': user.username})

    if request.method == 'POST' and 'submit_otp' in request.POST:
        otp = request.POST.get('otp')
        username = request.POST.get('username')

        user = User.objects.filter(username=username).first()
        otp_obj = OtpModel.objects.filter(user=user, otp=otp).first()

        if not otp_obj:
            messages.error(request, 'Invalid OTP')
            return render(request, 'submit-otp.html', {'username': username})

        # 🔥 expiry check (10 min)
        if timezone.now() > otp_obj.created_at + timedelta(minutes=10):
            otp_obj.delete()
            messages.error(request, 'OTP expired')
            return render(request, 'forget-password.html')

        otp_obj.delete()

        return render(request, 'change-password.html', {'username': username})
    if request.method == 'POST' and 'change_password' in request.POST:
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'change-password.html', {'username': username})

        user = User.objects.filter(username=username).first()
        print(user)
        print(new_password)

        user.set_password(new_password)
        user.save()

        messages.success(request, 'Password changed successfully')
        return redirect('login')

    return render(request, 'forgetpassword.html')