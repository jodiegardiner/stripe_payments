from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from django.conf.urls import url, include
from accounts import views as accounts_views


urlpatterns = [
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', accounts_views.subscriptions_webhook, name='subscriptions_webhook'),
    url(r'^007adceb-ab3e-4153-b4d6-d27f09673010/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]