from django.contrib import admin
from django.urls import path
import introduce.views

urlpatterns = [
    path('home',introduce.views.home, name='home'),
    path('post/<int:post_id>/',introduce.views.detail, name='detail'),
    path('post/new/',introduce.views.post_new,name='new'),
    path('post/<int:post_id>/edit',introduce.views.post_edit,name='edit'),
    path('post/<int:post_id>/delete',introduce.views.post_delete,name='delete'),    
]