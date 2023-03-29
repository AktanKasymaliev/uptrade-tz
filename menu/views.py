from django.shortcuts import render
from django.views import generic

from menu.models import Notes

class HomePage(generic.View):

    def get(self, request):
        return render(request, 'home_page.html')

class DetailPage(generic.View):

    def get(self, request, url):
        try:
            note = Notes.objects.get(url=url)
            return render(request, 'detail_page.html', {'note': note})
        except Notes.DoesNotExist:
            return render(request, 'error.html')