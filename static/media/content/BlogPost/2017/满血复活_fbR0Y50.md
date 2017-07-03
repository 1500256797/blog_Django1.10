我要使用这张图片了http://127.0.0.1:8000/media/filer/filer_public/e1/27/e127ec7f-d72a-4b3a-82bd-3a8d2c3e5dda/1_160818161836_1.jpg


不仅这样，我还要在md中使用这张图片
![这是我的！！！！][1]


  [1]: http://127.0.0.1:8000/media/filer/filer_public/e1/27/e127ec7f-d72a-4b3a-82bd-3a8d2c3e5dda/1_160818161836_1.jpg
  
  **Bug真的多哟！！**
  
  

    
urlpatterns = [
    url('^about/$', views.about),
    url(r'^(?P<slug>[-\w\d]+),(?P<post_id>\d+)/$', views.blogpost, name='blogposts'),
    # 博客记录
    url('^archive/$', views.archive),
    url('^article/(?P<freshness>.*)/$', views.article),
    url('^$', views.home),

]