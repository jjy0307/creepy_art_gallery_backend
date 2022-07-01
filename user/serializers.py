from rest_framework import serializers

from user.models import User as UserModel


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["user_id", "password", "username"]

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().update(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user
