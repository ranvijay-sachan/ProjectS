from django.utils.translation import ugettext as _

from rest_framework_simplejwt import exceptions
from rest_framework_simplejwt import authentication


class JSONWebTokenAuthentication(authentication.JWTAuthentication):
    """
        Overiding the default authenticate_credentials method of JWT.
        Since in our microservices, we dont need to verify token against UserModelObject,
        we will use the payload, decoded using secret key signature.
    """
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.

        Returns an active user.
        dynamically creating a class object and
        assigning the payload attributes to it, as if a user object from db is fetched.
        Also, dynamically assigning is_authenticated method to it.
        """
        user_id = validated_token.payload.get('user_id')
        is_superuser = validated_token.payload.get('is_superuser', False)
        user = validated_token.payload.get('user')
        permissions = validated_token.payload.get('permissions')
        if not all((user_id, user, permissions)):
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)
        payload = {}
        payload['user'] = user
        payload['user_id'] = user_id
        payload['is_superuser'] = is_superuser
        payload['permissions'] = permissions
        payload['is_authenticated'] = True
        user = type('MicroServiceUser', (object,), payload)
        user.is_authenticated = lambda: True

        return user
