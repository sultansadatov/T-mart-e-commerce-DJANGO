from django.http import HttpResponse, HttpRequest
from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

from django import forms
from django.forms import ModelForm
from core.models import Subscription


class SubscriptionForm(ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"

        widgets = {
            "email": forms.TextInput(attrs={"class": "email"}),
        }

def subscription_view(request: HttpRequest) -> HttpResponse:
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

    return {
        "subscription_form": form,
    }

