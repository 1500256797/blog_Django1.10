from collections import defaultdict

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import BlogPost, Category

'''
返回的是一个HttpResonse对象
'''
class HomeView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    context_object_name = 'blogposts'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.filter(name__isnull=False)
        return context




def blogpost(request, slug, post_id):
    args = {'blogpost': get_object_or_404(BlogPost, pk=post_id)}
    return render(request, 'blog/singlepost.html', args)

def get_sorted_posts(c):
    blogposts = BlogPost.objects.all()
    # defaultdict 使用list作为值的类型，当见不存在时，会自动生成一个list默认值
    posts_by_year = defaultdict(list)
    # posts_by_year=dict()
    # 根据类别找到文章
    posts_of_a_category = blogposts.filter(category=c)  # already sorted by pub_date
    print('-------------让我看看相同类别的文章-------------------')
    print(posts_of_a_category)
    # 将找到的文章
    return posts_of_a_category

def article(request, freshness):
    """ redirect to article accroding to freshness, latest->oldest:freshness=1->N """
    if freshness.isdigit():
        try:
            article_url = BlogPost.objects.all()[int(freshness) - 1].get_absolute_url()
            return redirect(article_url)
        except IndexError:
            raise Http404
        except AssertionError:  # freshness=0
            raise Http404
    else:
        return redirect('/')


