from rest_framework_simplejwt import serializers, views
# from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib import admin


class MyTokenObtainPairSerializer(serializers.TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['is_superuser'] = user.is_superuser
        token['permissions'] = list(user.user_permissions.all().values_list('codename', flat=True))
        # token['groups'] = user.groups
        token['user'] = user.username

        return token


class MyTokenObtainPairView(views.TokenViewBase):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = MyTokenObtainPairSerializer


custom_token_obtain_pair = MyTokenObtainPairView.as_view()

admin.site.register(Permission)