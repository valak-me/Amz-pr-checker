from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('update/', views.update,name='update'),
    path('delete/<int:pk>/', views.delete,name='delete'),
     path('search/', views.search,name='search'),
]
# :celery -A amz_pr_checker worker --loglevel=INFO -B