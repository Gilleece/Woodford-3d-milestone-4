from django.shortcuts import render
from marketing.forms import EmailSignupForm
from marketing.models import Signup

# Create your views here.


def index(request):
    """
    A view to return the index page and take mailing list signups
    """
    form = EmailSignupForm()
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {"form": form}
    return render(request, "home/index.html", context)
