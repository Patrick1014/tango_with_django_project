from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'), #/rango/index/
    path('about/', views.about, name='about'), #/rango/about/
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
]