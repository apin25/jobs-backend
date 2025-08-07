from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import ExpiringToken

class ExpiringTokenAuthentication(TokenAuthentication):
    model = ExpiringToken

    def authenticate_credentials(self, key):
        user, token = super().authenticate_credentials(key)
        if token.expired():
            token.delete() 
            raise AuthenticationFailed('Token has expired')
        return user, token
