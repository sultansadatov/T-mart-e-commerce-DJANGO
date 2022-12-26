"""tmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from itertools import product
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from core.views import set_language
from django.contrib.auth import views as auth_views #import this
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('product.urls')),
    path('', include('order.urls')),
    path('', include('users.urls', namespace="user")),
    path('', include('blog.urls')),

    path('api/', include('api.urls')),

    #path('accounts/', include('django.contrib.auth.urls')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_complete'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('search/', views.product_search, name='product_search'),
    path('oauth/', include('social_django.urls', namespace='social')),
]

urlpatterns += [
    *i18n_patterns(*urlpatterns, prefix_default_language=True),
   
   # YENİ
    path("set_language/<str:language>", set_language, name="set-language"),
]

# urlpatterns = [
#     *i18n_patterns(*urlpatterns, prefix_default_language=False),
#     ]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path('rosetta/', include('rosetta.urls'))
    ]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)