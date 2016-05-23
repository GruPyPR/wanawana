from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('events.urls')),
]
