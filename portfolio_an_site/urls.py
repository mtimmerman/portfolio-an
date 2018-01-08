from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from portfolio_an import views

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Portfolio pages
    
    url(r'^$', views.home, name="home"),    
    url(r'^blog/', include('portfolio_an.blog.urls')),
)

urlpatterns += patterns(
    # Internationalization

    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^i18n/setlang/$', views.set_language, name='set_language'),

    # Admin stuff
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^flats/', include('django.contrib.flatpages.urls')),
)

# Media
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
)
