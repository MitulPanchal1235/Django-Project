
from django.urls import path
from ImageDetection import views
urlpatterns = [
    path('',views.index ,name="index"),
    path('report/',views.report ,name="report"),
]