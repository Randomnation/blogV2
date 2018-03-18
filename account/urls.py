from django.urls import path, include
from django.contrib.auth.views import login, logout
from account import views

app_name = "account"

urlpatterns = [
    path('login/$', login, {'template_name': 'account/login.html'}, name='login'),
    path('logout/$', logout, {'template_name': 'account/logout.html'}, name='logout'),
    path('register/$', views.register, name='register'),
    path('login_success/$', views.login_success, name='login_success'),
    path('logout_success/$', views.logout_success, name='logout_success'),
    path('register_success/$', views.register_success, name='register_success'),
    path('not_verified/$', views.not_verified, name='not_verified'),
    path('login_next_test/$', views.login_next_test, name='login_next_test'),
    path('verify/(?P<user>.*)/(?P<code>.*)/$', views.verify, name='verify'),
    path('verify/$', views.verify, {'code': None, 'user': None}, name='verify')
]