from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyGenericEmplyerAPIViews




urlpatterns = [
    path('mygen', MyGenericEmplyerAPIViews.as_view()),
    path('mygen/<int:pk>/', MyGenericEmplyerAPIViews.as_view()),
]
