from api.v1.repositories.alias_repository import AliasRepository
from api.v1.serializers.alias_serializer import AliasSerializer


class AliasService:

    def __init__(self) -> None:
        self.repo = AliasRepository()

    def get_alias(self, id: int):
        alias = self.repo.get(id=id)
        if not alias:
            return None
        serializer = AliasSerializer(alias, many=False)
        return serializer.data

    def list_alias(self, filters: dict = None):
        alias = self.repo.list(filters=filters)
        serializer = AliasSerializer(alias, many=True)
        return serializer.data

    def create_alias(self, data: dict):
        print(data)
        print(data)
        print(data)
        serializer = AliasSerializer(data=data, partial=True)
        print("-------")
        if not serializer.is_valid():
            print(serializer.errors)
            return None
        serializer.save()
        return serializer.data

    def update_alias(self, id: int, data: dict):
        alias = self.repo.get(id=id)
        if not alias:
            return None
        serializer = AliasSerializer(alias, data=data, partial=True)
        if not serializer.is_valid():
            return None
        serializer.save()
        return serializer.data

    def delelete_alias(self, id: int):
        alias = self.repo.get(id=id)
        if not alias:
            return None
        alias.delete()
        return True
