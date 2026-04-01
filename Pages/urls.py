from django.urls import path, include
from .views import HomePageView

app_name = "Pages"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),         # Your landing page
]