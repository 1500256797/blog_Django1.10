import os
from datetime import datetime

from django.db import models
from django.utils import timezone

# for slug, get_absolute_url
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# delete md_file before delete/change model
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.files.base import ContentFile

import markdown2
from django.utils.html import strip_tags
from filer.fields.image import FilerImageField
from unidecode import unidecode
from taggit.managers import TaggableManager

import blog

upload_dir = 'content/BlogPost/%s/%s'

class Category(models.Model):
    '''
    Category 只要一个分类名就可以了
    '''
    name =models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    class Meta:
        ordering = ['-pub_date']    # ordered by pub_date descending when retriving
    def get_upload_md_name(self, filename):
        if self.pub_date:
            year = self.pub_date.year   # always store in pub_year folder
        else:
            year = datetime.now().year
        upload_to = upload_dir % (year, self.title + '.md')
        return upload_to

    def get_html_name(self, filename):
        if self.pub_date:
            year = self.pub_date.year
        else:
            year = datetime.now().year
        upload_to = upload_dir % (year, filename)
        return upload_to

    # 标题上限我暂时设置200
    title = models.CharField(max_length=200)
    # 存储比较短的字符串可以用CharField，但对于文章的正文来说可能会是一大段文本，所以我使用TextField
    # body,md_file.最终都转换成html_file来展示
    body = models.TextField(blank=True)
    html_file = models.FileField(upload_to=get_html_name, blank=True)    # generated html file
    md_file = models.FileField(upload_to=get_upload_md_name, blank=True)  # uploaded md file
    # 文章摘要，可以没有文章摘要，但默认情况下CharField 要求我们必须存入数据，否则会报错
    # 但是只要设置blank = True 就可以允许空值了。
    excerpt = models.TextField(max_length=200,blank=True)
    # 分别是发布时间和最后修改时间。
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    last_edit_date = models.DateTimeField('last edited', auto_now=True)

    # 用于记录文章访问量
    views = models.PositiveIntegerField(default=10)
    slug = models.SlugField(max_length=200, blank=True)
    index_image = FilerImageField(related_name='BlogPost_image')
    # 这是文章的分类，分类的模型我已经定义在上面。
    # 在这里我吧文章对应的数据库表和分类对应的数据表联系起来。
    # 在这里我规定一篇文章只能对应一个分类，所以说是一对一的联系。
    # 其实规定一篇文章有多个分类也可以。
    category = models.ForeignKey(Category)# 分类
    tags = TaggableManager()
    def __str__(self):
        return self.title   # 根据继承搜索流程,先是实例属性,然后就是类属性,所以这样用没问题
    @property
    def filename(self):
        if self.md_file:
            return os.path.basename(self.title)
        else:
            return 'no md_file'

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        # 如果没写body就要上传文件。
        if not self.body and self.md_file:
            self.body = self.md_file.read()
        html = markdown2.markdown(self.body,
                                  extras=["fenced-code-blocks", "tables"])
        self.html_file.save(self.title + '.html',
                            ContentFile(html.encode('utf-8')), save=False)
        self.html_file.close()
        # 如果没有填写摘要
        if not self.excerpt:

            # 首先实例化一个Markdown类，用于渲染文本
            md =markdown2.Markdown(extensions=[
                'markdown2.extensions.extra',
                'markdown2.extensions.codehilite',

            ])
            # 先将Markdown转成html，然后去除语法标签，取前54个字符赋值到except
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super(BlogPost,self).save(*args, **kwargs)


    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])

    def display_html(self):
        '''
        无论写没写body，最终都展示的是htnl_file
        '''
        with open(self.html_file.path, encoding='utf-8') as f:
            return f.read()
    def get_absolute_url(self):
        return reverse(blog.views.blogpost,

                       kwargs={'slug': self.slug, 'post_id': self.id})

@receiver(pre_delete, sender=BlogPost)
def blogpost_delete(instance, **kwargs):
        if instance.md_file:
            instance.md_file.delete(save=False)
        if instance.html_file:
            instance.html_file.delete(save=False)

# 文章和图片是1对N关系。所以
class BlogPostImage(models.Model):

    def get_upload_img_name(self, filename):
        upload_to = upload_dir % ('images', filename)  # filename involves extension
        return upload_to

    blogpost = models.ForeignKey(BlogPost, related_name='images')
    image = models.ImageField(upload_to=get_upload_img_name)

