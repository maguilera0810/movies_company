from api.base.repositories.base_repository import BaseRepository
from apps.movie.models import Movie


class MovieRepository(BaseRepository):

    def get(self, id):
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return None

    def list(self, filters: dict = None):
        if filters is None:
            filters = {}
        return Movie.objects.filter(**filters)

    def delete(self, id):
        if movie := self.get(id=id):
            movie.delete()
            return True
        return False
