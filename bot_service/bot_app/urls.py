from django.urls import path

from . import views

urlpatterns = [
    path('start/', views.start_test),
    path('stop/', views.stop_test)
]