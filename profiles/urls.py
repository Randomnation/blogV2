from django.urls import path, re_path
from profiles import views

app_name = "profiles"

urlpatterns = [
    path('user/<int:pk>/', views.user_profile, name='user_profile'),
    path('user/<int:pk>/update/', views.user_profile_edit, name='update_profile'),
]