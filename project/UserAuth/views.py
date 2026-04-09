from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import OtpModel
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


def ForgetPassword(request):

    if request.method == 'POST' and 'send_otp' in request.POST:
        username_or_email = request.POST.get('username_or_email') # can be either username or email
        if not username_or_email:
            messages.error(request, 'Please enter your username or email')
            return redirect('forget-password')
        else:
            user = None
            email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if '@' in username_or_email and re.match(email_regex, username_or_email):   
                try:
                    user = User.objects.get(email=username_or_email)
                    print(user)
                except User.DoesNotExist:
                    messages.error(request, f'No user found with this email {username_or_email}')
                    return redirect('forget-password')
            else:
                try:
                    user = User.objects.get(username=username_or_email)
                except User.DoesNotExist:
                    messages.error(request, f'No user found with this username {username_or_email}')
                    return redirect('forget-password')
                
        # generate OTP and send email logic here
        otp = random.randint(1000, 9999)
        new_otp = OtpModel(user=user, otp=otp)
        new_otp.save()
        # send email to user.email with the otp

        try:
            send_mail(
                'Your OTP for Password Reset', # email subject
                f'Your OTP for password reset is {otp}. It is valid for 10 minutes.', # email body
                settings.DEFAULT_FROM_EMAIL, # from email
                [user.email], # to email
                fail_silently=False, # in case of error, it will raise an exception instead of failing silently
            )
        except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')
                return redirect('forget-password')
        
        messages.success(request, f'An OTP has been sent to your email {user.email}')
        return render(request, 'submit-otp.html', {'user': user})

    if request.method == 'POST' and 'resend_otp' in request.POST:
        pass

    if request.method == 'POST' and 'submit_otp' in request.POST:
        pass

    if request.method == 'POST' and 'change_password' in request.POST:
        pass

    return render(request, 'forgetpassword.html')