from django.urls import path
from .views import RegisterView, CreateTweetView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tweet/', CreateTweetView.as_view(), name='create_tweet'),
]
