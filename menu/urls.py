from django.urls import path

from menu.views import HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="home_page"),
]
