from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('/category/<slug:category>', views.category, name='category'),
    path('/detail/(?P<title>[^/]+)$', views.detail, name='detail'),
    
]
