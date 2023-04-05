from django.urls import path
from .views import landing_function

urlpatterns = [
    path("", landing_function, name="landing-page")
]
