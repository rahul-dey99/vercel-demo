from django.urls import path
from vercel_demo.views import index

urlpatterns = [
    path('', index)
]