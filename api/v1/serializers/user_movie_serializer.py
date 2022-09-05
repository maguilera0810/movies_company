from api.v1.serializers.alias_serializer import AliasSerializer
from api.v1.serializers.genre_serializer import GenreSerializer
from api.v1.serializers.movie_serializer import MovieSerializer
from api.v1.serializers.user_serializer import UserSerializer
from apps.authentication.models import Alias
from apps.movie.models import Movie
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class MoviePublicSerializer(ModelSerializer):
    genres = SerializerMethodField("get_genres")
    casting = SerializerMethodField("get_casting")
    producers = SerializerMethodField("get_producers")
    directors = SerializerMethodField("get_directors")

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

    def get_genres(self, instance):
        serializer = GenreSerializer(instance.genres, many=True)
        return serializer.data

    def get_casting(self, instance):
        serializer = UserSerializer(instance.casting, many=True)
        return serializer.data

    def get_producers(self, instance):
        serializer = UserSerializer(instance.producers, many=True)
        return serializer.data

    def get_directors(self, instance):
        serializer = UserSerializer(instance.directors, many=True)
        return serializer.data


class UserPublicSerializer(ModelSerializer):
    aliases = SerializerMethodField("get_aliases")
    movies_as_actor = SerializerMethodField("get_movies_as_actor")
    movies_as_producer = SerializerMethodField("get_movies_as_producer")
    movies_as_director = SerializerMethodField("get_movies_as_director")

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "aliases",
            "movies_as_actor",
            "movies_as_producer",
            "movies_as_director",
        )

    def get_aliases(self, instance):
        alias = Alias.objects.filter(user=instance)
        serializer = AliasSerializer(alias, many=True)
        return serializer.data

    def get_movies_as_actor(self, instance):
        movies = instance.movie_casting.all()
        serializer = MovieSerializer(movies, many=True)
        return serializer.data

    def get_movies_as_producer(self, instance):
        movies = instance.movie_producers.all()
        serializer = MovieSerializer(movies, many=True)
        return serializer.data

    def get_movies_as_director(self, instance):
        movies = instance.movie_directors.all()
        serializer = MovieSerializer(movies, many=True)
        return serializer.data
