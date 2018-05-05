from django.conf import settings
from django.contrib import messages
from django.core.serializers import serialize
from django.http import HttpResponse
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.views.generic import CreateView, DetailView, TemplateView, View
from django_filters.views import FilterView

from . import filters
from .forms import ClaimForm
from .models import Category, Claim


class ClaimCreateView(CreateView):

    template_name = 'claims/claim_create.html'
    model = Claim
    form_class = ClaimForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'request': self.request,
        })
        return kwargs

    def get_success_url(self, **kwargs):
        messages.success(self.request, _('Claim created, thanks for report a claim'))
        return reverse('claims:claim-list')


class ClaimListView(FilterView):

    template_name = 'claims/claim_list.html'
    model = Claim
    paginate_by = settings.PAGINATION_DEFAULT_PAGE_SIZE
    context_object_name = 'claims'
    filterset_class = filters.ClaimFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
        })
        return context


class ClaimDetailView(DetailView):

    template_name = 'claims/claim_detail.html'
    model = Claim
    context_object_name = 'claim'
    pk_url_kwarg = 'id'


class MapView(TemplateView):

    template_name = 'claims/map.html'


class MapDataView(View):

    def get(self, request, *args, **kwargs):
        qs = Claim.objects.exclude(point=None)
        data = serialize(
            'claim-geojson', qs, geometry_field='point',
            fields=('address', 'description', 'date',),
        )
        return HttpResponse(data, content_type='application/json')
