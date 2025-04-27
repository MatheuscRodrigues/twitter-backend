from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

from .models import Follow, Tweet
from .serializers import UserSerializer, TweetSerializer, FollowSerializer

User = get_user_model()

# View de registro de novo usuario
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View que permite a criacao de tweets
class CreateTweetView(generics.CreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View para seguir usuários
class FollowUserView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # O follower é o usuário logado
        serializer.save(follower=self.request.user)

# View para listar o feed
class FeedView(generics.ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Busca os usuários que o logado está seguindo
        following_users = Follow.objects.filter(follower=self.request.user).values_list('following', flat=True)
        # Filtra tweets apenas desses usuários
        return Tweet.objects.filter(user__in=following_users).order_by('-created_at')

# View para deixar de seguir
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        following_id = request.data.get('following')
        if not following_id:
            return Response({'error': 'É necessário informar o ID do usuário a deixar de seguir.'}, status=400)

        try:
            follow = Follow.objects.get(follower=request.user, following_id=following_id)
            follow.delete()
            return Response({'detail': 'Unfollow realizado com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
        except Follow.DoesNotExist:
            return Response({'error': 'Você não está seguindo este usuário.'}, status=400)
        
# View feed personalizado
class TweetFeedView(ListAPIView):
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Lista os usuários que o usuário autenticado segue
        followed_users = Follow.objects.filter(follower=self.request.user).values_list('following_id', flat=True)

        # Inclui também os próprios tweets
        return Tweet.objects.filter(user__in=list(followed_users) + [self.request.user.id]).order_by('-created_at')
    
# View de recuperação de senha
class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        new_password = request.data.get('new_password')

        if not email or not new_password:
            return Response({'error': 'Email and new password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            return Response({'detail': 'Password reset successfully.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)
