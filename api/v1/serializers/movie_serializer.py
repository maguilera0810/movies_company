from apps.movie.models import Movie
from rest_framework.serializers import ModelSerializer


class MovieSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "code",
            "release",
            "status",
            "genres",
            "casting",
            "producers",
            "directors",
        )
