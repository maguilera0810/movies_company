from api.base.repositories.base_repository import BaseRepository
from apps.movie.models import Genre


class GenreRepository(BaseRepository):

    def get(self, id):
        try:
            return Genre.objects.get(id=id)
        except Genre.DoesNotExist:
            return None

    def list(self, filters: dict = None):
        if filters is None:
            filters = {}
        return Genre.objects.filter(**filters)

    def delete(self, id):
        if genre := self.get(id=id):
            genre.delete()
            return True
        return False
