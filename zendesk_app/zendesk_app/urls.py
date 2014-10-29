from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import SuspendedTicketsView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="tickets.html"), name='home'),
    url(r'^zendesk/suspended_tickets/$', SuspendedTicketsView.as_view(), name='suspended_tickets'),
)
