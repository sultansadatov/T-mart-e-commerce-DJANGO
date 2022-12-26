from django.http import HttpResponse, HttpRequest
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.shortcuts import render
from core.forms import ContactForm, SearchForm 
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages 
from django.contrib.auth import get_user_model
from product.models import Product
from core.forms import SubscriptionForm
from django.urls.base import resolve, reverse
from blog.models import *

User = get_user_model()


# Create your views here.


from django.shortcuts import render,redirect

from product.models import Category, Product, Tag
from django.views.generic import ListView, CreateView


# Create your views here.
class Index(ListView):
    model = Category
    context_object_name = 'categories'
    paginate_by = 8
	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()[:3]
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        return context





def about(request):
    return render(request, "core/about.html")

def contact(request: HttpRequest) -> HttpResponse:
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()

    context =  {
        "contact_form": form,
    }
    return render(request, "core/contact.html", context = context)

def team(request):
    return render(request, "core/team.html")


def set_language(request, language='en'):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
    next_url = request.META.get("HTTP_REFERER")
    if next_url:
        translation.activate(language)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response



def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'tmartsultan@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})






def product_search(request):
	
	query = request.GET["query"]

	products = Product.objects.filter(product_name=query)
	context = {'products':products,}

	return render(request, 'core/search.html', context)


