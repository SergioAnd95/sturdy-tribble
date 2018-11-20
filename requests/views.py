from django.views.generic import ListView

from core.mixins import AdminRequiredMixin

from .models import Request
# Create your views here.


class LatestRequestsListView(AdminRequiredMixin, ListView):
    queryset = Request.objects.all()[:10]
    context_object_name = 'requests'
    template_name = 'requests/request_list.html'
