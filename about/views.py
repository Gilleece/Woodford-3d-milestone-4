from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm


def about(request):
    """
    A view to return the about page
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Successfully sent message!")
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data["message"]
            send_mail(
                email_subject,
                email_message,
                settings.CONTACT_EMAIL,
                settings.ADMIN_EMAIL,
            )
            return redirect(reverse("about"))
        else:
            messages.error(
                request,
                "Failed to send message. \
                    Please ensure the form is valid.",
            )
    form = ContactForm()
    context = {"form": form}
    return render(request, "about/about.html", context)
