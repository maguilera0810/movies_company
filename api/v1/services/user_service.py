from api.v1.repositories.user_repository import UserRepository
from api.v1.serializers.user_movie_serializer import UserPublicSerializer
from api.v1.serializers.user_serializer import UserSerializer
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User

{
    "username": "mauricio@gmail.com",
    "first_name": "Mauricio",
    "last_name": "Aguilera",
    "email": "mauricio@gmail.com",
    "password": "123456",
    "is_staff": False,
    "is_active": True,
    "is_superuser": False,
}


class UserService:

    def __init__(self) -> None:
        self.repo = UserRepository()

    def get_user(self, id: int):
        user = self.repo.get(id=id)
        if not user:
            return None
        serializer = UserPublicSerializer(user, many=False)
        return serializer.data

    def list_users(self, filters: dict = None):
        users = self.repo.list(filters=filters)
        serializer = UserPublicSerializer(users, many=True)
        return serializer.data

    def create_user(self, data: dict):
        hashed_pw = make_password(data["password"])
        user = User(
            username=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=hashed_pw,
            is_staff=data.get("is_staff", False),
            is_active=data.get("is_active", True),
            is_superuser=data.get("is_superuser", False),
        )
        user.save()
        # In the case you have another fileds to person you can add as follow
        # user.person.field_name = field_value
        serializer = UserPublicSerializer(user, partial=True)
        return serializer.data

    def update_user(self, id: int, data: dict):
        user = self.repo.get(id=id)
        if not user:
            return None
        serializer = UserPublicSerializer(user, data=data, partial=True)
        if not serializer.is_valid():
            return None
        serializer.save()
        return serializer.data

    def delelete_user(self, id: int):
        user = self.repo.get(id=id)
        if not user:
            return None
        user.delete()
        return True
