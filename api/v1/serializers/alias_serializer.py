from apps.authentication.models import Alias
from rest_framework.serializers import ModelSerializer


class AliasSerializer(ModelSerializer):

    class Meta:
        model = Alias
        fields = (
            "id",
            "user",
            "name",
        )
