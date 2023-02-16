from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users import views


urlpatterns = [
    path('users/create/', views.UserViewSet.as_view({'post': 'create_user'})),
    path('users/verify/', views.UserViewSet.as_view({'post': 'verify_user'})),
    path('users/token/', views.UserViewSet.as_view({'post': 'create_token'})),
    path('users/token/verify/', views.UserViewSet.as_view({'post': 'verify_token'})),
    path('auth/', include('djoser.urls')),
    # path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]