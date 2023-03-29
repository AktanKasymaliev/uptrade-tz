from django.urls import path

from menu.views import HomePage
from menu.views import DetailPage

urlpatterns = [
    path("", HomePage.as_view(), name="home_page"),
    path("<slug:url>/", DetailPage.as_view(), name="note_detail")
]