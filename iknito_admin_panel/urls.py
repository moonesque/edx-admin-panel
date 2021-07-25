"""
URLs for iknito_admin_panel.
"""
from django.conf.urls import url  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from . import views

urlpatterns = [
    # TODO: Fill in URL patterns and views here.
    # url(r'', TemplateView.as_view(template_name="iknito_admin_panel/base.html")),
    # my test view
    url("hello-edx", views.HelloEdx.as_view())
]
