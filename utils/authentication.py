# utils/authentication.py
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.authtoken.models import Token
from datetime import timedelta
from django.utils import timezone

class ExpiringTokenAuthentication(TokenAuthentication):
    keyword = "Bearer" 

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted.')

        if timezone.now() - token.created > timedelta(days=1):
            raise AuthenticationFailed('Token has expired.')

        return (token.user, token)

