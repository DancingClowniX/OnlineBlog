from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import News
from django.http import HttpResponseRedirect
from datetime import datetime

def main(request):
    if request.method == "POST":
        text = request.POST.get("news")
        News.objects.create(text=text)
        return HttpResponseRedirect("/post")
    elif request.method == "GET":
        results = News.objects.all()
        data = {
        "news" : results
        }
        return render(request, "main.html", context=data)

def edit_news(request, news_id):
    newsData = News.objects.get(id=news_id)
    if request.method == "GET":
        data = {"id": news_id,
                "text": newsData.text,}
        return render(request, "edit_news.html", data)
    if request.method =="POST":
        text = request.POST.get("news")
        newsData.text = text
        newsData.save()
        return HttpResponseRedirect("/post")

def delete_news(request, news_id):
    try:
        news_content = News.objects.get(id=news_id).delete()
        return HttpResponseRedirect("/post")
    except News.DoesNotExist:
        return HttpResponseNotFound("""<a href=""><h2>Новость не найдена</h2><a>""")
