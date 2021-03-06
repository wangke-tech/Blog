#-*- encoding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Article(models.Model):
    title = models.CharField(max_length = 100)#博客题目
    category = models.CharField(max_length = 50,blank = True)#博客标签
    date_time = models.DateTimeField(auto_now_add = True) #博客日期
    content = models.TextField(blank = True,null = True)#博客文章正文
    read_times = models.IntegerField(max_length = 10,blank=False,default=0)#阅读次数
    migration_flag = models.BooleanField(blank=False,default=False)
    def __unicode__(self):
        return self.title
    
    def get_absolute_urls(self):
        path = reverse('detail',kwargs={'id':self.id})
        return 'http://127.0.0.1:8000%s'%path

    class Meta:#按时间降序
        ordering = ['-date_time']
