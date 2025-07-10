from django.urls import path
from .views import AboutPageView, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]