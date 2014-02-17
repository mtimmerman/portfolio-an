from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Portfolio pages

    url(r'^$', TemplateView.as_view(template_name='portfolio_an/home.html'), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='portfolio_an/about.html'), name="about"),
    url(r'^services/$', TemplateView.as_view(template_name='portfolio_an/services.html'), name="services"),
    url(r'^contact/$', TemplateView.as_view(template_name='portfolio_an/contact.html'), name="contact"),
    url(r'^faq/$', TemplateView.as_view(template_name='portfolio_an/faq.html'), name="faq"),

    # Admin stuff

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    # Internationalization

    (r'^i18n/', include('django.conf.urls.i18n')),
)
