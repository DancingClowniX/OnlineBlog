from django.urls import path,re_path

import post.views as post

urlpatterns = [
    path('',post.main, name = 'main_url'),
    path('edit_news/<int:news_id>/', post.edit_news),
    path('delete_news/<int:news_id>/', post.delete_news),
]