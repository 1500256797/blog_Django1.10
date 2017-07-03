from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from blog import views

admin.autodiscover()

urlpatterns =[
    # blog
    # url(r'^(?P<page>\d*)/$',views.home,name='home'),
    url(r'^blog/',include('blog.urls')),
    url(r'^$', views.home, name='home'),
    # admin
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^filer/',include('filer.urls')),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

