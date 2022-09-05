import threading

from api.v1.repositories.movie_repository import MovieRepository
from api.v1.serializers.movie_serializer import MovieSerializer
from api.v1.serializers.user_movie_serializer import MoviePublicSerializer
from resources.enums.enums import StatusEnum
from resources.gateways.delay_gateway import DelayGateway


class MovieService:

    def __init__(self) -> None:
        self.repo = MovieRepository()

    def get_movie(self, id: int):
        movie = self.repo.get(id=id)
        if not movie:
            return None
        serializer = MoviePublicSerializer(movie, many=False)
        return serializer.data

    def list_movies(self, filters: dict = None):
        movies = self.repo.list(filters=filters)
        serializer = MoviePublicSerializer(movies, many=True)
        return serializer.data

    def create_movie(self, data: dict):
        serializer = MovieSerializer(data=data, partial=True)
        if not serializer.is_valid():
            return None
        serializer.save()
        return serializer.data

    def update_movie(self, id: int, data: dict):
        movie = self.repo.get(id=id)
        if not movie:
            return None
        serializer = MovieSerializer(movie, data=data, partial=True)
        if not serializer.is_valid():
            return None
        serializer.save()
        return serializer.data

    def delelete_movie(self, id: int):
        movie = self.repo.get(id=id)
        if not movie:
            return None
        movie.delete()
        return True

    def enabled_movie(self, id: int):
        movie = self.repo.get(id=id)
        if not movie:
            return None
        thread_process = threading.Thread(
            target=DelayGateway().call_api_delay,
            name="call_delay_api",
            args=()
        )
        thread_process.start()
        movie.status = StatusEnum.enabled.value
        movie.save()
        return True
