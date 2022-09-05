from api.v1.repositories.genre_repository import GenreRepository
from api.v1.serializers.genre_serializer import GenreSerializer


class GenreService:

    def __init__(self) -> None:
        self.repo = GenreRepository()

    def get_genre(self, id: int):
        genre = self.repo.get(id=id)
        if not genre:
            return None
        serializer = GenreSerializer(genre, many=False)
        return serializer.data

    def list_genres(self, filters: dict = None):
        genres = self.repo.list(filters=filters)
        serializer = GenreSerializer(genres, many=True)
        return serializer.data

    def create_genre(self, data: dict):
        serializer = GenreSerializer(data=data, partial=True)
        if not serializer.is_valid():
            return None
        serializer.save()
        return serializer.data

    def update_genre(self, id: int, data: dict):
        genre = self.repo.get(id=id)
        if not genre:
            return None
        serializer = GenreSerializer(genre, data=data, partial=True)
        if not serializer.is_valid():
            return None
        serializer.save()
        return serializer.data

    def delelete_genre(self, id: int):
        genre = self.repo.get(id=id)
        if not genre:
            return None
        genre.delete()
        return True
