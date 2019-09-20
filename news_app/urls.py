from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('sports/',views.sports,name='sports'),
    path('yemennews/',views.yemennews,name='yemennews'),


]