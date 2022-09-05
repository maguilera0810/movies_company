from rest_framework.response import Response
from rest_framework import status
from api.v1.services.alias_service import AliasService
from api.base.controllers.base_controller import IsAuthController


class AliasController(IsAuthController):

    def list_alias(self, request):
        filters = {
            "user": request.user.id,
        }
        service = AliasService()
        alias = service.list_alias(filters=filters)
        return Response(alias, status=status.HTTP_200_OK)

    def retrieve_alias(self, request, id: int):
        service = AliasService()
        alias = service.get_alias(id=id)
        if not alias:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        return Response(alias, status=status.HTTP_200_OK)

    def create_alias(self, request):
        print("create_alias")
        data = request.data
        data["user"] = request.user.id
        service = AliasService()
        alias = service.create_alias(data=data)
        if not alias:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response(alias, status=status.HTTP_200_OK)

    def update_alias(self, request, id: int):
        data = request.data
        service = AliasService()
        alias = service.update_alias(id=id,
                                     data=data)
        if not alias:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response(alias, status=status.HTTP_200_OK)

    def delete_alias(self, request, id: int):
        service = AliasService()
        is_deleted = service.delelete_alias(id=id)
        if not is_deleted:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)
