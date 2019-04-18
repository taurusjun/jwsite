from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from rebin.models import Accomment


class MyView(View):
    def get(self, request):
        # <view logic>
        acm = Accomment.objects.order_by('-updatedate').first()
        quoteid = acm.quoteid;
        acm2 = Accomment.objects.get(cid=quoteid)
        return HttpResponse("Hello, world. You're at the rebin index.")

class ACCommentsDetailsView(TemplateView):
    # queryset = Accomment.objects.filter(acid='10130324').order_by('-updatedate')
    # context_object_name = 'accm_list'
    template_name = 'blog-item.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ACCommentsDetailsView, self).get_context_data(**kwargs)
        acid = self.request.GET.get('acid')
        if acid:
            # Add in a QuerySet of all the books
            acqs = Accomment.objects.filter(acid=acid).order_by('-updatedate')
            # acqs = Accomment.objects.filter(acid='10130324').order_by('-updatedate')
            # aclts = [{"username":"1","cid":"2","quoteid":"3","postdate":"4","content":5}]
            aclts = []
            for idx, record in enumerate(acqs):
                rec = record.toJSON()
                quotes = []
                quoteid = record.quoteid
                while(quoteid and quoteid!=0):
                    try:
                        quoteCM = Accomment.objects.get(cid=quoteid)
                        quoteid = quoteCM.quoteid
                        quotes.append(quoteCM.toJSON())
                    except ObjectDoesNotExist:
                        quoteid = None
                rec['quotes']=quotes
                aclts.append(rec)
            context['accm_list'] = aclts
        return context