from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Max
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from rebin.models import Accomment, Actopic


class MyView(View):
    def get(self, request):
        # <view logic>
        acm = Accomment.objects.order_by('-updatedate').first()
        quoteid = acm.quoteid;
        acm2 = Accomment.objects.get(cid=quoteid)
        return HttpResponse("Hello, world. You're at the rebin index.")

class IndexView(TemplateView):
    # queryset = Accomment.objects.filter(acid='10130324').order_by('-updatedate')
    # context_object_name = 'accm_list'
    # template_name = 'index.html'
    template_name = 'onepage-index.html'


class ACTopicListView(ListView):

    context_object_name = 'actopic_list'
    template_name = 'blog.html'
    paginate_by = 10

    # 搜索功能
    def get_queryset(self):
        searchText = self.request.GET.get('searchFor');
        default = self.request.GET.get('default');

        if not searchText and default:
            self.queryset = Accomment.objects \
                .select_related() \
                .filter(content__contains='[img=图片]') \
                .values('acid', 'acid__topic') \
                .annotate(cnt=Count('acid')) \
                .annotate(latest=Max('postdate')) \
                .order_by('-latest')

        if (not searchText) and (not default):
            self.queryset = Accomment.objects \
                .select_related() \
                .values('acid', 'acid__topic') \
                .annotate(cnt=Count('acid')) \
                .annotate(latest=Max('postdate')) \
                .order_by('-latest')

        if searchText:
            self.queryset = Accomment.objects \
                .select_related() \
                .filter(content__contains=searchText) \
                .values('acid', 'acid__topic') \
                .annotate(cnt=Count('acid')) \
                .annotate(latest=Max('postdate')) \
                .order_by('-latest')


        return super().get_queryset();


class ACCommentsDetailsView(TemplateView):
    # queryset = Accomment.objects.filter(acid='10130324').order_by('-updatedate')
    # context_object_name = 'accm_list'
    template_name = 'blog-item.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ACCommentsDetailsView, self).get_context_data(**kwargs)
        acid = self.request.GET.get('acid')
        actopic = Actopic.objects.get(acid=acid)
        context['actopic'] = actopic
        if acid:
            acqs = Accomment.objects.filter(acid=acid).order_by('-updatedate')
            # acqs = Accomment.objects.filter(acid='10130324').order_by('-updatedate')
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