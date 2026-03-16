from django.urls import re_path
from pretix.multidomain import event_url

from .views import EventCssJsSettingsView, CustomCssView, CustomJsView

event_patterns = [
    event_url(r'^event_css_js/custom\.css$', CustomCssView.as_view(), name='custom.css'),
    event_url(r'^event_css_js/custom\.js$', CustomJsView.as_view(), name='custom.js'),
]

urlpatterns = [
    re_path(
        r'^control/event/(?P<organizer>[^/]+)/(?P<event>[^/]+)/event_css_js/settings$',
        EventCssJsSettingsView.as_view(),
        name='settings',
    ),
]
