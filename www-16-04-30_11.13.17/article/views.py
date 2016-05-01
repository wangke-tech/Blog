from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

def home(Request):
    post_list = Article.objects.all()
    return render(Request,'home.html',{'post_list':post_list})
def test(Request):
    return render(Request,'test.html',{'current_time':datetime.now()})
def details(Request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(Request,'post.html',{'post':post})

