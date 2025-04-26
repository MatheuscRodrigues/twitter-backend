from django.urls import path
from .views import LikeToggleAPIView, RetweetAPIView, CommentCreateAPIView

urlpatterns = [
    path('like/<int:tweet_id>/', LikeToggleAPIView.as_view(), name='like-toggle'),
    path('retweet/<int:tweet_id>/', RetweetAPIView.as_view(), name='retweet'),
    path('comment/<int:tweet_id>/', CommentCreateAPIView.as_view(), name='comment'),
]
