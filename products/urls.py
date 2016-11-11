from products import views as product_views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', product_views.all_products),
]