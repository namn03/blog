# coding: utf-8
from __future__ import unicode_literals
from django.contrib import admin

from django.db import models

from redactor.fields import RedactorField


class LargeCategory(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    menu_text = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40, null=False)
    url = models.CharField(max_length=10, null=False)
    large_category = models.ForeignKey(LargeCategory, null=True)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)

    opt = {
        }
    content = RedactorField(null=False, redactor_options=opt)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    comments = models.PositiveSmallIntegerField(default=0, null=True)
    main_image = models.ImageField(upload_to='%Y/%m/', null=True, blank=True)
    hide = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.image.delete()
        super(Post, self).delete()


class Comment(models.Model):
    name = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=32, null=False)
    content = models.TextField(null=False)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


# Create your models here.
