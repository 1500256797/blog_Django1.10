![图1][1]

**Django 个人博客之MARKDOWN**
  再正式介绍前，请欣赏一组图片。
  ![此处输入图片的描述][2]


  图文混合编辑，更牛逼！！！继续。。。
  ![此处输入图片的描述][3]


  [1]: http://127.0.0.1:8000/media/filer/filer_public/5e/2c/5e2c2c35-be21-4145-b39c-4e54c7311bc5/xia-zai-_1.jpg
  [2]: http://127.0.0.1:8000/media/filer/filer_public/1a/1b/1a1b7b4b-5ea2-4f6e-a97e-f78ccd5e46e6/xia-zai-_2.jpg
  [3]: http://127.0.0.1:8000/media/filer/filer_public/eb/c6/ebc63758-8ed0-4e3d-813e-5872382584cc/xia-zai-_3.jpg
  

        title = models.CharField(max_length=200)
    # 存储比较短的字符串可以用CharField，但对于文章的正文来说可能会是一大段文本，所以我使用TextField
    # body,md_file.最终都转换成html_file来展示
    body = models.TextField(blank=True)
    html_file = models.FileField(upload_to=get_html_name, blank=True)    # generated html file
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)  # uploaded md file
    # 文章摘要，可以没有文章摘要，但默认情况下CharField 要求我们必须存入数据，否则会报错
    # 但是只要设置blank = True 就可以允许空值了。
    excerpt = models.CharField(max_length=200,blank=True)
    # 分别是发布时间和最后修改时间。
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    last_edit_date = models.DateTimeField('last edited', auto_now=True)
    
    **Markdown 代码展示部分，不够美观。**
    下一步操作：
    

 1. 直接写
 2. 上传md文件

**继续更新：**
为什么首页的图片不显示？？？？？？？这又是嘛问题？？？？

**30号晚更新**
将{{blogpost.index_image|safe}}后面加。url就能解决首页图片不显示问题。{{blogpost.index_image.url|safe}}

问题，Description字段并没有什么作用，所以可以删掉吧》