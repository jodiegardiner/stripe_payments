from django.conf.urls import url, include
from hello.views import get_index


urlpatterns = [
    url(r'^$', get_index, name='index'),
]