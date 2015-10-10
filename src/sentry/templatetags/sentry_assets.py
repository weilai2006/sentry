from __future__ import absolute_import

from django.template import Library

from sentry.utils.assets import get_asset_url

register = Library()


@register.simple_tag
def asset_url(module, path):
    """
    Returns a versioned asset URL (located within Sentry's static files).

    Example:
      {% asset_url 'sentry' 'dist/sentry.css' %}
      =>  "/_static/74d127b78dc7daf2c51f/sentry/dist/sentry.css"
    """
    return get_asset_url(module, path)