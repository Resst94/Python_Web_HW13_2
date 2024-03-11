from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<str:author_name>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('delete_quote/<quote_id>', views.delete_quote, name='delete_quote'),
    path('tag/<str:tag_name>/', views.TagQuotesView.as_view(), name='tag_quotes'),
]
