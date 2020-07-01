from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .models import FollowedCrypto
from .serializers import FollowedCryptoSerializer, UserSerializer


# Create your views here.


class FollowedCryptoViewSet(viewsets.ModelViewSet):
    queryset = FollowedCrypto.objects.all()
    serializer_class = FollowedCryptoSerializer
    permission_classes = [AllowAny,]

    def create(self, request, *args, **kwargs):
        if request.data:
            name = request.data['name']
            coin_id = request.data['coin_id']
            token = request.data['token']

            try:
                FollowedCrypto.objects.create(
                    name=name,
                    coin_id=coin_id,
                    who_follow=Token.objects.get(key=token).user
                )

                response = {'message': 'Dodano do śledzonych!'}
                return Response(response, status=status.HTTP_200_OK)
            except:
                response = {'message': 'Coś poszło źle!.'}
                return Response(response, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['POST'], detail=False)
    def get_followed_by_user(self, request):
        try:
            token = request.data['token']
            followed = FollowedCrypto.objects.filter(who_follow=Token.objects.get(key=token).user)

            serializer = FollowedCryptoSerializer(followed, many=True)
            response = {'result': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['POST'], detail=False)
    def delete_followed_by_user(self, request):
        try:
            token = request.data['token']
            coin_id = request.data['coin_id']
            followed = FollowedCrypto.objects.filter(who_follow=Token.objects.get(key=token).user)
            followed.filter(coin_id=coin_id).delete()

            response = {'message': 'Usunięto'}
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response(None, status=status.HTTP_403_FORBIDDEN)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]
