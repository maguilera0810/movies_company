from api.base.controllers.base_controller import IsAuthController
from api.v1.services.genre_service import GenreService
from rest_framework import status
from rest_framework.response import Response


class GenreController(IsAuthController):

    def list_genres(self, request):
        genres = GenreService().list_genres()
        return Response(genres, status=status.HTTP_200_OK)

    def retrieve_genre(self, request, id: int):
        genre = GenreService().get_genre(id=id)
        if not genre:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        return Response(genre, status=status.HTTP_200_OK)

    def create_genre(self, request):
        data = request.data
        genre = GenreService().create_genre(data=data)
        if not genre:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response(genre, status=status.HTTP_200_OK)

    def update_genre(self, request, id: int):
        data = request.data
        genre = GenreService().update_genre(id=id,
                                            data=data)
        if not genre:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response(genre, status=status.HTTP_200_OK)

    def delete_genre(self, request, id: int):
        is_deleted = GenreService().delelete_genre(id=id)
        if not is_deleted:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)
