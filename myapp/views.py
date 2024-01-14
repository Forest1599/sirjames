from django.shortcuts import render, HttpResponse

from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm
 
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                success = handlePost(request)

                if(success):
                    messages.success(request, 'Your email has been sent successfully!')
                else:
                    messages.error(request, 'Failed to process the form. Please try again..')
            
            except Exception as e:
                messages.error(request, f'An error has occured, please try again..')
        else:
            messages.error(request, 'Form failed to validate, please try again..')


            return HttpResponseRedirect(request.path_info)

    return render(request, "contact.html")

def home(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                success = handlePost(request)

                if(success):
                    messages.success(request, 'Your email has been sent successfully!')
                else:
                    messages.error(request, 'Failed to process the form. Please try again..')
            
            except Exception as e:
                messages.error(request, f'An error has occured, please try again..')
        else:
            messages.error(request, 'Form failed to validate, please try again..')


            return HttpResponseRedirect(request.path_info)

    return render(request, "index.html")

def gallery(request):
    return render(request, "gallery.html")


def handlePost(request):
    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']


    email_body = loader.render_to_string(
            "email.html",
            {'name': name,
            'email': email,
            'message': message}
    )

    mailSent = send_mail(
        "SirJamesLocks email from website " + name,
        message,
        email,
        ["sirjames-locks@hotmail.com"],
        html_message=email_body,
        fail_silently=False
    )

    return mailSent

        