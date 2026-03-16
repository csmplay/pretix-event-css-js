from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View
from pretix.control.views.event import EventSettingsFormView, EventSettingsViewMixin

from .forms import EventCssJsSettingsForm

CACHE_MAX_AGE = 3600 * 24 * 365  # 1 year — URL changes on content update


class EventCssJsSettingsView(EventSettingsViewMixin, EventSettingsFormView):
    form_class = EventCssJsSettingsForm
    template_name = 'pretix_event_css_js/control_settings.html'

    def get_success_url(self):
        return reverse('plugins:pretix_event_css_js:settings', kwargs={
            'organizer': self.request.organizer.slug,
            'event': self.request.event.slug,
        })


class CustomCssView(View):
    def get(self, request, *args, **kwargs):
        css = request.event.settings.get('event_css_js_css', default='')
        response = HttpResponse(css or '', content_type='text/css; charset=utf-8')
        if 'v' in request.GET:
            response['Cache-Control'] = 'public, max-age={}'.format(CACHE_MAX_AGE)
        return response


class CustomJsView(View):
    def get(self, request, *args, **kwargs):
        js = request.event.settings.get('event_css_js_js', default='')
        response = HttpResponse(js or '', content_type='application/javascript; charset=utf-8')
        if 'v' in request.GET:
            response['Cache-Control'] = 'public, max-age={}'.format(CACHE_MAX_AGE)
        return response
