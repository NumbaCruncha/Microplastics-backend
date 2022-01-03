
from django.db.models import query
from .serializers import UserSerializer, RegisterSerializer, ChangePasswordSerializer, UpdateUserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework import generics, status, viewsets
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken
from rest_framework.response import Response
from django.contrib.auth import get_user


class CurrentUserView(APIView):
    def get(self, request):
        current_user = request.user
        serializer = UserSerializer(current_user)
        return Response(serializer.data)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = (IsAuthenticated)

   

#     def get_object(self):
#         pk = self.kwargs.get('pk')

#         if pk == self.request.id:
#             return self.request.user

   

#         return super(UserViewSet, self).get_object()


    # def get_user(request, primary_key):
    #     try:
    #         user = User.objects.get(pk=primary_key)
    #     except Exception:
    #         'Oops'

    
    
    # def get_object(self):
    #     pk = self.kwargs.get('pk')

    
    #     if pk == self.request.user.id:
    #         return self.request.user

    #     return super(UserViewSet, self).get_object()



class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)