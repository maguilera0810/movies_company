from api.v1.controllers.alias_controller import AliasController
from api.v1.controllers.genre_controller import GenreController
from api.v1.controllers.movie_controller import MovieController
from api.v1.controllers.user_controller import UserController
from django.urls import path


urlpatterns = [
    path('genre/',
         GenreController.as_view({'get': 'list_genres',
                                  'post': 'create_genre',
                                  }),
         name='genre_controller'),
    path('genre/<int:id>',
         GenreController.as_view({'put': 'update_genre',
                                  'get': 'retrieve_genre',
                                  'delete': 'delete_genre',
                                  }),
         name='genre_id_controller'),
]

urlpatterns += [
    path('movie/',
         MovieController.as_view({'get': 'list_movies',
                                  'post': 'create_movie',
                                  }),
         name='movie_controller'),
    path('movie/<int:id>',
         MovieController.as_view({'put': 'update_movie',
                                  'get': 'retrieve_movie',
                                  'delete': 'delete_movie',
                                  }),
         name='movie_id_controller'),
    path('movie/<int:id>/enabled/',
         MovieController.as_view({'put': 'enabled_movie'}),
         name='movie_id_controller'),
]

urlpatterns += [
    path('user/',
         UserController.as_view({'get': 'list_users',
                                 'post': 'create_user',
                                 }),
         name='user_controller'),
    path('user/<int:id>',
         UserController.as_view({'put': 'update_user',
                                 'get': 'retrieve_user',
                                 'delete': 'delete_user',
                                 }),
         name='user_id_controller'),

]

urlpatterns += [
    path('user/alias/',
         AliasController.as_view({'get': 'list_alias',
                                  'post': 'create_alias',
                                  }),
         name='alias_controller'),
    path('user/alias/<int:id>',
         AliasController.as_view({'put': 'update_alias',
                                  'get': 'retrieve_alias',
                                  'delete': 'delete_alias',
                                  }),
         name='alias_id_controller'),
]
