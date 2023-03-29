from django.shortcuts import render
from django.views import generic

from menu.models import Notes

class HomePage(generic.View):

    def get(self, request):
        return render(request, 'home_page.html', {'notes': Notes.objects.all()})

class DetailPage(generic.View):
    pass
    # def get(self, request, ):
