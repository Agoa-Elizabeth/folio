from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == 'POST':
        # Handle form data here (email, save, etc.)
        pass
    return render(request, 'contact.html')

#contact.html


def contact_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # You can use send_mail if email is configured
        # send_mail(f"Contact from {name}", message, email, ["you@example.com"])

        messages.success(request, "Thanks for reaching out! I'll respond shortly.")
        return render(request, "portfolio/contact.html")
    
    return render(request, "portfolio/contact.html")

#each project view
def projects_page(request):
    return render(request, 'projects.html')

def project1(request):
    return render(request, 'project1.html')

def project2(request):
    return render(request, 'project2.html')

def project3(request):
    return render(request, 'project3.html')

#email functionality
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = f"Contact from {name}"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            full_message,
            email,  # from email
            ['elizabethagoa@gmail.com'],  
            fail_silently=False,
        )
        messages.success(request, "Thanks for reaching out! I'll respond shortly.")
        return render(request, 'contact.html')
    return render(request, 'contact.html')
