��Ҫʹ������ͼƬ��http://127.0.0.1:8000/media/filer/filer_public/e1/27/e127ec7f-d72a-4b3a-82bd-3a8d2c3e5dda/1_160818161836_1.jpg


�����������һ�Ҫ��md��ʹ������ͼƬ
![�����ҵģ�������][1]


  [1]: http://127.0.0.1:8000/media/filer/filer_public/e1/27/e127ec7f-d72a-4b3a-82bd-3a8d2c3e5dda/1_160818161836_1.jpg
  
  **Bug��Ķ�Ӵ����**
  
  

    
urlpatterns = [
    url('^about/$', views.about),
    url(r'^(?P<slug>[-\w\d]+),(?P<post_id>\d+)/$', views.blogpost, name='blogposts'),
    # ���ͼ�¼
    url('^archive/$', views.archive),
    url('^article/(?P<freshness>.*)/$', views.article),
    url('^$', views.home),

]