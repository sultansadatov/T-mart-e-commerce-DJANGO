from django import forms
from django.forms import ModelForm
from core.models import Contact

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

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["your_name", "email", "subject", "message"]

        widgets = {
            "email": forms.TextInput(attrs={"class": "email"}),
            "your_name": forms.TextInput(attrs={"placeholder": "Your Name*"}),
            "email": forms.TextInput(attrs={"placeholder": "Mail*"}),
            "subject": forms.TextInput(attrs={"placeholder": "Subject*"}),
            "message": forms.Textarea(attrs={"placeholder": "Message*", "rows": 1}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(label = 'Search', max_length=100)