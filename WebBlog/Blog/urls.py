from django.urls import path, include
from . import views

app_name = 'Blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.DeleteView.as_view(), name='delete'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('error/', views.ErrorView.as_view(), name='error')
]