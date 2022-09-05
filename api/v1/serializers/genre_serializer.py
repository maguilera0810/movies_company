from apps.movie.models import Genre
from rest_framework.serializers import ModelSerializer


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
            "code",
        )
