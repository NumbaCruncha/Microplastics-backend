from django.urls import path
from auth.views import UserDetailView, CurrentUserView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView, LogoutAllView
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'user', UserDetailView, 'user')

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/user/', CurrentUserView.as_view(), name='user'),
    path('login/user/<int:pk>/', UserDetailView.as_view(), name='user_details'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),
]