from django.urls import path, re_path
from dataAnalysis import views

app_name = "dataAnalysis"

urlpatterns = [
    path('heatmap/', views.heatmap_index, name='comment_heatmap')
    # path('user/<int:pk>/update/', views.user_profile_edit, name='update_profile'),
]