from django.urls import path
from .views import RegisterView, LoginView, UserProfileView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserProfileView.as_view(), name='user-profile'),
]
