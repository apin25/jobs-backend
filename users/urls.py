from django.urls import path
from .views import LoginView, LogoutView, RegisterView, get_user_by_token

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('me/<str:token_key>', get_user_by_token, name="me")
]
