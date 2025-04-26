from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Like, Retweet
from accounts.models import Tweet

# View para curtir ou descurtir um tweet
class LikeToggleAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        tweet_id = self.kwargs.get('tweet_id')
        tweet = Tweet.objects.get(id=tweet_id)
        like, created = Like.objects.get_or_create(user=request.user, tweet=tweet)

        if not created:
            like.delete()
            return Response({'message': 'Tweet unliked'}, status=status.HTTP_200_OK)
        return Response({'message': 'Tweet liked'}, status=status.HTTP_201_CREATED)

# View para retweetar um tweet
class RetweetAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        tweet_id = self.kwargs.get('tweet_id')
        tweet = Tweet.objects.get(id=tweet_id)
        Retweet.objects.create(user=request.user, tweet=tweet)
        return Response({'message': 'Retweeted successfully'}, status=status.HTTP_201_CREATED)

# View para comentar em um tweet
class CommentCreateAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        tweet_id = self.kwargs.get('tweet_id')
        content = request.data.get('content')
        parent_tweet = Tweet.objects.get(id=tweet_id)
        Tweet.objects.create(user=request.user, content=content, parent=parent_tweet)
        return Response({'message': 'Comment added'}, status=status.HTTP_201_CREATED)
