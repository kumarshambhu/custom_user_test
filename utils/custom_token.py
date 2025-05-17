from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['name'] = user.name
        token['role'] = user.type
        token['phone'] = user.phone
        print(f"{user.username}, {user.name}, {user.type}, {user.phone}")
        return token
