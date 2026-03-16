from django import forms
from django.utils.translation import gettext_lazy as _
from pretix.base.forms import SettingsForm


class EventCssJsSettingsForm(SettingsForm):
    event_css_js_css = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 12, 'class': 'monospace'}),
        label=_('Custom CSS'),
        required=False,
        help_text=_('Custom CSS rules that will be loaded on every presale page of this event.'),
    )
    event_css_js_js = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 12, 'class': 'monospace'}),
        label=_('Custom JavaScript'),
        required=False,
        help_text=_(
            'Custom JavaScript that will be loaded at the end of every presale page of this event. '
            'Use with care — incorrect code may break the shop experience for your customers.'
        ),
    )
