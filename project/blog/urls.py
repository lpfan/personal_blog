from django.conf.urls import patterns, url
from django.views.generic import ListView

from models import Category


blog_urls = patterns('',
    url(
        r'^categories$',
        ListView.as_view(template_name='blog/blog_categories.html', model=Category),
        name='categories'
    ),
)
