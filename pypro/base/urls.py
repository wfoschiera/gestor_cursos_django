from django.urls import path
from pypro.base.views import home, trigger_error_sentry


app_name = "base"
urlpatterns = [
    path("", home, name="home"),
    path("sentry-debug/", trigger_error_sentry),
]
