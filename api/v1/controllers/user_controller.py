from api.base.controllers.base_controller import IsAdminController, BaseController
from api.v1.services.user_service import UserService
from rest_framework import status
from rest_framework.response import Response


class UserController(IsAdminController):

    def create_user(self, request):
        data = request.data
        service = UserService()
        if user := service.create_user(data=data):
            return Response(user, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve_user(self, request, id: int):
        service = UserService()
        if user := service.get_user(id=id):
            return Response(user, status=status.HTTP_200_OK)
        return Response(user, status=status.HTTP_404_NOT_FOUND)

    def list_users(self, request):
        service = UserService()
        users = service.list_users()
        return Response(users, status=status.HTTP_200_OK)

    def update_user(self, request, id: int):
        service = UserService()
        data = request.data
        if user := service.update_user(id=id,
                                       data=data):
            return Response(user, status=status.HTTP_200_OK)
        return Response(user, status=status.HTTP_400_BAD_REQUEST)

    def delete_user(self, request, id: int):
        return Response({}, status=status.HTTP_200_OK)
