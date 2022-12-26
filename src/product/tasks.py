from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task

from product.services.products import get_popular_products

from core.models import Subscription
User = get_user_model()

@shared_task()
def send_new_product_notifications() -> None:
    
    now = timezone.now() + timedelta(hours=4)
    print("nossfafsfasdfasdfasf", now)
    users_emails = User.objects.all().values_list('email', flat=True)
    
    print(users_emails)
    products = get_popular_products()
    context = {
        "products": products,
    }
    html_content = render_to_string('tasks/email-subscribers.html', context=context)
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(
        "New Products",
        text_content,
        settings.EMAIL_HOST_USER,
        users_emails,
        # ['sultan.sadatov.2018@gmail.com',]
        # ['gunelvalishova@gmail.com',]
        )

    email.attach_alternative(html_content, "text/html")
    email.send()


@shared_task()
def send_new_product_to_subscribers() -> None:
    
    subscribers = Subscription.objects.all().values_list('email', flat=True)
    
    print(subscribers)
    products = get_popular_products()
    context = {
        "products": products,
    }
    html_content = render_to_string('tasks/email-subscribers.html', context=context)
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(
        "New Products",
        text_content,
        settings.EMAIL_HOST_USER,
        subscribers,
        # ['sultan.sadatov.2018@gmail.com',]
        # ['gunelvalishova@gmail.com',]
        )

    email.attach_alternative(html_content, "text/html")
    email.send()
