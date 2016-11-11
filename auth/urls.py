"""auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views import static
from settings import MEDIA_ROOT
from django.contrib import admin
from accounts import urls as accounts_urls
from hello import urls as hello_urls
from magazines import urls as magazines_urls
from paypal_store import urls as paypal_urls
from products import urls as products_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^account/', include(accounts_urls)),
    url(r'', include(hello_urls)),
    url(r'^magazines/', include(magazines_urls)),
    url(r'^store/', include(paypal_urls)),
    url(r'^products/', include(products_urls)),

]
