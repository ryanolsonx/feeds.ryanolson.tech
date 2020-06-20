from django.urls import path

from myfeeds import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.FeedDetailView.as_view(), name='feed_detail'),
    path('<int:pk>/rss', views.FeedView.as_view(), name='feed'),
]