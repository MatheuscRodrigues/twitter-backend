from django.urls import path
from .views import FeedView, FollowUserView, RegisterView, CreateTweetView, TweetFeedView, UnfollowUserView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tweet/', CreateTweetView.as_view(), name='create_tweet'),
    path('follow/', FollowUserView.as_view(), name='follow-user'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('feed/', TweetFeedView.as_view(), name='tweet-feed'),
]
