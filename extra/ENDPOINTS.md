Endpoints
=========

Below is a list of the available endpoints, which will have 3 types of  [permissions](#permissions) :

- [JWT](#jwt)
- [User](#user)
- [Alias](#alias)
- [Movie](#movie)
- [Genre](#genre)

---------

# Permissions

- All Users :green_circle:
- Auth Users :yellow_circle:
- Admin Users :red_circle: :red_circle:

# JWT

## Get Token

- Method: POST
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/token/
```

- Example Request:

```json
{
    "username": maguilera0810@gmail.com,
    "pasword": "123456"
}
```

- Example Response:

```json
# status 200
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2Mjg1NjQxOCwiaWF0IjoxNjYyMjUxNjE4LCJqdGkiOiJlYjhhNzJmZjc3OWI0ZGZlOGNlYTgzODg0NjU0YzlhMCIsInVzZXJfaWQiOjV9.v75DvVOoRuhPkwfisAyz6PWztyrN5_zkVXCYR4_Z-2E",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyMjk0ODE4LCJpYXQiOjE2NjIyNTE2MTgsImp0aSI6IjYwNGIzNGIxYjJhZDRiMGQ5MmNmNDU4Mzg0MGExMTM4IiwidXNlcl9pZCI6NX0.vnCTjUBrmYSxD6Xu_ca_ls4QhMriYShYIKlYdMUtyF0"
}
```

## Refresh Token

- Method: POST
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/refresh/
```

- Example Request:

```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2Mjg1NjQxOCwiaWF0IjoxNjYyMjUxNjE4LCJqdGkiOiJlYjhhNzJmZjc3OWI0ZGZlOGNlYTgzODg0NjU0YzlhMCIsInVzZXJfaWQiOjV9.v75DvVOoRuhPkwfisAyz6PWztyrN5_zkVXCYR4_Z-2E"
}
```

- Example Response:

```json
# status 200
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyMjk1MTE2LCJpYXQiOjE2NjIyNTE2MTgsImp0aSI6IjNiOGRjNWUzMTZjNTRmYTU5ZmI5NmI3MzJlZGY3ZDE4IiwidXNlcl9pZCI6NX0.OJ1qGTRgutQaygK5noW5dkfhYQ-DssjvoVbVfr_rmPs"
}
```

## Verify Token

- Method: POST
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/verify/
```

- Example Request:

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYyMjk1MTE2LCJpYXQiOjE2NjIyNTE2MTgsImp0aSI6IjNiOGRjNWUzMTZjNTRmYTU5ZmI5NmI3MzJlZGY3ZDE4IiwidXNlcl9pZCI6NX0.OJ1qGTRgutQaygK5noW5dkfhYQ-DssjvoVbVfr_rmPs"
}
```

- Example Response:

```json
# status 200
{}
```

---

# User

## Create User

- Method: POST
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/v1/user/
```

- Example Request:

```json
{
    "first_name": "Mauricio",
    "last_name": "Aguilera",
    "email": "mauricio+006@gmail.com",
    "password": "123456",
    "is_staff": true,
    "is_active": true,
    "is_superuser": false
}
```

- Example Response:

```json
# status 201
{
    "id": 6,
    "first_name": "Mauricio",
    "last_name": "Aguilera",
    "email": "mauricio+006@gmail.com",
    "username": "mauricio+006@gmail.com",
    "aliases": [...],
    "movies_as_actor": [...],
    "movies_as_producer": [...],
    "movies_as_director": [...]
}
```

## Get User

- Method: GET
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/user/{{user_id}}
```

- Example Response:

```json
# status 200
{
    "id": 6,
    "first_name": "Mauricio",
    "last_name": "Aguilera",
    "email": "mauricio+006@gmail.com",
    "username": "mauricio+006@gmail.com",
    "aliases": [...],
    "movies_as_actor": [...],
    "movies_as_producer": [...],
    "movies_as_director": [...]
}
```

## List Users

- Method: GET
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/user/
```

- Example Response:

```json
# status 200
[ 
    ... ,
    {
        "id": 6,
        "first_name": "Mauricio",
        "last_name": "Aguilera",
        "email": "mauricio+006@gmail.com",
        "username": "mauricio+006@gmail.com",
        "aliases": [...],
        "movies_as_actor": [...],
        "movies_as_producer": [...],
        "movies_as_director": [...]
    },
    ...
]
```

## Update User

- Notes:
  - The user only will be able to update his own data
- Method: PUT
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/verify/
```

- Example Request:

```json
{
    "first_name": "Mauricio",
    "last_name": "Aguilera",
    "email": "mauricio+006@gmail.com",
    "password": "123456",
    "is_staff": true,
    "is_active": true,
    "is_superuser": false
}
```

- Example Response:

```json
# status 201
{
    "id": 6,
    "first_name": "Mauricio",
    "last_name": "Aguilera",
    "email": "mauricio+006@gmail.com",
    "username": "mauricio+006@gmail.com",
    "aliases": [...],
    "movies_as_actor": [...],
    "movies_as_producer": [...],
    "movies_as_director": [...]
}
```

## Delete User

- Method: DELETE
- Permissions:
  - Admin Users :red_circle:

```
{{url}}/api/v1/user/{{user_id}} 
```

- Example Response:

```json
# status 201
{}
```

---

# Alias

## Create Alias

- Note:
  - Users will only be able to create their own aliases
- Method: POST
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/user/alias/
```

- Example Request:

```json
{
    "name": "Pepito"
}
```

- Example Response:

```json
# status 201
{
    "id": 6,
    "name": "Pepito",
    "user": 1,
}
```

## Get Alias

- Method: GET
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/v1/user/alias/{{alias_id}}
```

- Example Response:

```json
# status 200
{
    "id": 6,
    "name": "Pepito",
    "user": 1,
}
```

## List Alias

- Method: GET
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/v1/user/alias/
```

- Example Response:

```json
# status 200
[ 
    ... ,
    {
        "id": 6,
        "name": "Pepito",
        "user": 1
    },
    ...
]
```

## Update Alias

- Note:
  - Users will only be able to update their own aliases
- Method: PUT
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/user/alias/{{alias_id}}
```

- Example Request:

```json
{
    "name": "Manolo"
}
```

- Example Response:

```json
# status 201
{
  "id": 6,
  "name": "Manolo",
  "user": 1
}
```

## Delete Alias

- Note:
  - Users will only be able to delete their own aliases
- Method: DELETE
- Permissions:
  - All Users :green_circle:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/user/alias/{{alias_id}}
```

- Example Response:

```json
# status 200
{}
```

---

# Movie

## Create Movie

- Method: POST
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/movie/
```

- Example Request:

```json
{
  "title": "Star Wars",
  "release": "1977-05-25",
  "genres": [ 2, 3, 4 ],
  "casting": [ 1, 2, 3 ],
  "producers": [ 2 ],
  "directors": [ 3]
}
```

- Example Response:

```json
# status 201
{
  "id": 1,
  "title": "Star Wars",
  "release": "1977-05-25",
  "code": "movie-1",
  "status": "draft",
  "genres": [ ... ],
  "casting": [ ... ],
  "producers": [ ... ],
  "directors": [ ... ]
}
```

## Get Movie

- Method: GET
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/v1/movie/{{movie_id}}
```

- Example Response:

```json
# status 200
{
  "id": 1,
  "title": "Star Wars",
  "release": "1977-05-25",
  "code": "movie-1",
  "status": "draft",
  "genres": [ ... ],
  "casting": [ ... ],
  "producers": [ ... ],
  "directors": [ ... ]
}
```

## List Movies

- Method: GET
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/v1/movie/
```

- Example Response:

```json
# status 200
[ 
  ... ,
  {
    "id": 1,
    "title": "Star Wars",
    "release": "1977-05-25",
    "code": "movie-1",
    "status": "draft",
    "genres": [ ... ],
    "casting": [ ... ],
    "producers": [ ... ],
    "directors": [ ... ]
  },
  ...
]
```

## Update Movie

- Method: PUT
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/movie/{{movie_id}}
```

- Example Request:

```json
{
  "title": "King Lion",
  "release": "2005-04-21",
  "genres": [ 2, 3, 4 ],
  "casting": [ 1, 2, 3 ],
  "producers": [ 2 ],
  "directors": [ 3 ]
}
```

- Example Response:

```json
# status 200
{
  "id": 1,
  "title": "King Lion",
  "release": "2005-04-21",
  "code": "movie-1",
  "status": "draft",
  "genres": [ ... ],
  "casting": [ ... ],
  "producers": [ ... ],
  "directors": [ ... ]
}
```

## Delete Movie

- Method: DELETE
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/movie/{{movie_id}}
```

- Example Response:

```json
# status 200
{}
```

---

# Genre

## Create Genre

- Method: POST
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/genre/
```

- Example Request:

```json
{
  "name": "Suspenso"
}
```

- Example Response:

```json
# status 201
{
    "id": 1,
    "name": "Suspenso",
    "code": "genre-1"
}
```

## Get Genre

- Method: GET
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/v1/genre/{{genre_id}}
```

- Example Response:

```json
# status 200
{
  "id": 1,
  "name": "Suspenso",
  "code": "genre-1"
}
```

## List Genres

- Method: GET
- Permissions:
  - All Users :green_circle:

```
{{url}}/api/v1/genre/
```

- Example Response:

```json
# status 200
[ 
  ... ,
  {
    "id": 1,
    "name": "Suspenso",
    "code": "genre-1"
  },
  ...
]
```

## Update Genre

- Method: PUT
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/movie/{{movie_id}}
```

- Example Request:

```json
{
  "name": "Terror"
}
```

- Example Response:

```json
# status 200
{
  "id": 1,
  "name": "Terror",
  "code": "genre-1"
}
```

## Delete Genre

- Method: DELETE
- Permissions:
  - Auth Users :yellow_circle:

```
{{url}}/api/v1/genre/{{genre_id}}
```

- Example Response:

```json
# status 200
{}
```
