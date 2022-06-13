"""filedriver URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from users import views as users_view
from django.conf import settings
from django.conf.urls.static import static
from main import views as main_view

urlpatterns = [
    path("", main_view.index, name="index"),
    path("upload", main_view.upload_file, name="upload"),
    path('accounts/login/', users_view.loginPage, name="login"),
    path('accounts/logout/', users_view.logoutPage, name="logout"),
    path('accounts/register/', users_view.registerationPage, name="register"),
    path('accounts/verification/', users_view.verification, name="email-verification"),
    path('accounts/passwordReset/', users_view.password_reset, name="password-reset"),
    path('accounts/passwordResetConform/', users_view.password_check, name="password-reset-conf"),
    path('accounts/passwordResetForm/', users_view.password_set_form, name="password-reset-form"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)