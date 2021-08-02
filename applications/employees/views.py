from django.shortcuts import render
from django.views.generic import View
from .models import CardEmployees
# Create your views here.


class CardView(View):

    def get(self, request):
        card = CardEmployees.objects.all()
        return render(request, 'index.html', context={'card': card})
