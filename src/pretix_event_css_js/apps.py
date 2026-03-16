from django.utils.translation import gettext_lazy
from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_event_css_js"
    verbose_name = "Event CSS & JS"

    class PretixPluginMeta:
        name = gettext_lazy("Event CSS & JS")
        author = "Nico Knoll"
        description = gettext_lazy("Inject custom CSS and JavaScript into the presale pages of individual events.")
        visible = True
        version = __version__
        category = "CUSTOMIZATION"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA

    def uninstalled(self, event):
        event.settings.delete('event_css_js_css')
        event.settings.delete('event_css_js_js')
