from api.base.repositories.base_repository import BaseRepository
from django.contrib.auth.models import User


class UserRepository(BaseRepository):

    def get(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def get_by_email(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
    
    def list(self, filters: dict = None):
        if filters is None:
            filters = {}
        return User.objects.filter(**filters)

    def delete(self, id):
        if user := self.get(id=id):
            user.delete()
            return True
        return False
