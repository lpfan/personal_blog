import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )

    title = models.CharField(max_length=100)
    posted = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    category = models.ForeignKey('blog.Category')
    tags = models.ManyToManyField('blog.Tag')
    author = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField(_('allow comments'), default=True)

    def __unicode__(self):
        return '%s'%(self.title,)

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug':self.slug})


class Category(models.Model):
    title = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __unicode__(self):
        return '%s'%(self.title,)

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug':self.slug})


class Tag(models.Model):
    title = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)

    def __unicode__(self):
        return '%s'%(self.title,)

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug':self.slug})
