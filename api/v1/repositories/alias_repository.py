from api.base.repositories.base_repository import BaseRepository
from apps.authentication.models import Alias


class AliasRepository(BaseRepository):

    def get(self, id):
        try:
            return Alias.objects.get(id=id)
        except Alias.DoesNotExist:
            return None

    def list(self, filters: dict = None):
        if filters is None:
            filters = {}
        return Alias.objects.filter(**filters)

    def delete(self, id):
        if alias := self.get(id=id):
            alias.delete()
            return True
        return False
