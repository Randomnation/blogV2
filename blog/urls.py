from django.urls import path, re_path
from blog import views

app_name = "blog"

urlpatterns = [

    # Site Nav

    path('/', views.post_list, name='index'),
    # path(r'^api/', views.api_root, name='api'),
    # path(r'^blog/', views.post_list),
    # re_path(r'^/post/detail/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path('/post/detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('/post/new/', views.post_new, name='post_new'),
    # path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # path(r'^categories/add/$', views.add_categories, name='add_categories'),
    # path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    # path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    # path(r'^post/remove-all/$', views.post_remove_all, name='post_remove_all'),
    # path(r'^post/category/(?P<pk>\d+)/$', views.cat_post, name='cat_post'),
    # path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    # path(r'^comment/(?P<pk>\d+)/remove/main/$', views.comment_remove_main, name='comment_remove_main'),
]