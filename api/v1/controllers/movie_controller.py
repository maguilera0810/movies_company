from api.base.controllers.base_controller import IsAuthController
from api.v1.services.movie_service import MovieService
from rest_framework import status
from rest_framework.response import Response


class MovieController(IsAuthController):

    def list_movies(self, request):
        service = MovieService()
        movies = service.list_movies()
        return Response(movies, status=status.HTTP_200_OK)

    def retrieve_movie(self, request, id: int):
        service = MovieService()
        movie = service.get_movie(id=id)
        if not movie:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        return Response(movie, status=status.HTTP_200_OK)

    def create_movie(self, request):
        data = request.data
        service = MovieService()
        movie = service.create_movie(data=data)
        if not movie:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response(movie, status=status.HTTP_200_OK)

    def update_movie(self, request, id: int):
        data = request.data
        service = MovieService()
        movie = service.update_movie(id=id,
                                     data=data)
        if not movie:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response(movie, status=status.HTTP_200_OK)

    def delete_movie(self, request, id: int):
        service = MovieService()
        is_deleted = service.delelete_movie(id=id)
        if not is_deleted:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({}, status=status.HTTP_200_OK)
