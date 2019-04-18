from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from rebin.models import Accomment


class MyView(View):
    def get(self, request):
        # <view logic>
        cnt = Accomment.objects.count();
        return HttpResponse("Hello, world. You're at the rebin index."+str(cnt))

class Home(TemplateView):
    template_name = 'blog-item.html'

# def index(request):
#     return HttpResponse("Hello, world. You're at the rebin index.")