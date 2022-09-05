from api.v1.serializers.alias_serializer import AliasSerializer
from apps.authentication.models import Alias
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class UserSerializer(ModelSerializer):
    aliases = SerializerMethodField("get_aliases")

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "aliases",
        )

    def get_aliases(self, instance):
        alias = Alias.objects.filter(user=instance)
        serializer = AliasSerializer(alias, many=True)
        return serializer.data


