
import hashlib

from django.dispatch import receiver
from django.urls import resolve, reverse
from django.utils.translation import gettext_lazy as _
from pretix.control.signals import nav_event_settings
from pretix.multidomain.urlreverse import eventreverse
from pretix.presale.signals import html_footer, html_head


def _content_hash(content):
    return hashlib.md5(content.encode('utf-8')).hexdigest()[:12]


@receiver(nav_event_settings, dispatch_uid='event_css_js_nav_settings')
def navbar_settings(sender, request, **kwargs):
    url = resolve(request.path_info)
    return [{
        'label': _('Event CSS & JS'),
        'url': reverse('plugins:pretix_event_css_js:settings', kwargs={
            'event': request.event.slug,
            'organizer': request.organizer.slug,
        }),
        'active': url.namespace == 'plugins:pretix_event_css_js' and url.url_name == 'settings',
    }]


@receiver(html_head, dispatch_uid="pretix_event_css_js_html_head")
def r_html_head(sender, request=None, **kwargs):
    css = sender.settings.get('event_css_js_css', default='')
    if css and css.strip():
        url = eventreverse(sender, 'plugins:pretix_event_css_js:custom.css')
        url += '?v=' + _content_hash(css)
        return '<link rel="stylesheet" type="text/css" href="{}">'.format(url)
    return ''


@receiver(html_footer, dispatch_uid="pretix_event_css_js_html_footer")
def html_foot_presale(sender, request=None, **kwargs):
    js = sender.settings.get('event_css_js_js', default='')
    if js and js.strip():
        url = eventreverse(sender, 'plugins:pretix_event_css_js:custom.js')
        url += '?v=' + _content_hash(js)
        return '<script src="{}"></script>'.format(url)
    return ''
