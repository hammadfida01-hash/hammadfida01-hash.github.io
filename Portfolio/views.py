from django.shortcuts import render, redirect
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            subject=f'Portfolio Contact: {name}',
            message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
            from_email='hammadfida01@gmail.com',
            recipient_list=['hammadfida01@gmail.com'],
        )
        success = True

    return render(request, 'contact.html', {'success': success})