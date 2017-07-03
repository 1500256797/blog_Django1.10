from django.conf import settings
from django.conf.urls import url

from django.conf.urls.static import static

from . import views


urlpatterns = [
    url(r'^(?P<slug>[-\w\d]+),(?P<post_id>\d+)/$', views.blogpost, name='blogposts'),
    url('^article/(?P<freshness>.*)/$', views.article),
    url('^$', views.home),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
