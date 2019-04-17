from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View


class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse("Hello, world. You're at the rebin index.")

class Home(TemplateView):
    template_name = 'blog-item.html'

# def index(request):
#     return HttpResponse("Hello, world. You're at the rebin index.")