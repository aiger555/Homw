from django.urls import path
from .views import MainPage, NewsDetailView

urlpatterns = [
    path('', MainPage.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail_url')
]