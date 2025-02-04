from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload', views.UploadView.as_view(), name='upload'),
    path('api/', views.MeiboListView.as_view()),
    path('api/<int:pk>', views.MeiboDetailView.as_view()),
]