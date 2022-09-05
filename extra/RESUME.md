# Resume

[Back to main readme](../README.md)

# Requirements

1. Provide a REST API to access movies and persons models. ✅ ([see](ENDPOINTS.md#endpoints))
2. Safe methods are publicly available, no authentication is required. ✅ ([see](ENDPOINTS.md#permissions))
3. Unsafe methods are only available to authenticated users. ✅ ([see](ENDPOINTS.md#permissions))
4. Movie documents must include references or full documents to persons in their different roles. ✅ ([see](ENDPOINTS.md#list-movies))
5. Person documents must include references or full documents to movies in the different roles the Person has. ✅ ([see](ENDPOINTS.md#list-users))
6. For every movie you need to create a slug (maybe you heard of it as a ‘fake id’ or ‘friendly id’?). Explain the solution. ✅

    **Explanation**

    I first thought of using [slugify]("https://docs.djangoproject.com/en/4.1/ref/utils/#django.utils.text.slugify"), but ran into the case where this data was used as a reference for other things (eg locales), this would require more maintenance, so I chose to create the slug on save instance with a combination of model name and id

    ```python
    # Movie Model Example save method
    def save(self, *args, **kwargs):
        adding = self._state.adding
        super(Movie, self).save(*args, **kwargs)
        if adding:
            self.code = f"movie-{self.id}"
            self.save()

    ```

# Extra feature

1. **When a movie is created, it is created with draft status ✅**
2. **To mark a movie as enabled, an endpoint must be run. ✅** ([see](ENDPOINTS.md#enabled-movie))
3. **Each time a movie is marked as enabled, an external API must be called to report the status change. Since that API is known to take a long time to respond, the call is expected to be executed asynchronously (or in background), so as not to block the execution thread. Let's simulate the API call using deelay.me with 6 seconds: <https://deelay.me/5000/> ✅** ([see](/resources/gateways/delay_gateway.py))

    **Explanation:**

    I created a gateway that call this external api, and use [threading](https://docs.python.org/3/library/threading.html) to manage the task on background:

    ```python
    # Movie Service Method
    import threading
    def enabled_movie(self, id: int):
        movie = self.repo.get(id=id)
        if not movie:
            return None
        thread_process = threading.Thread(
            target=DelayGateway().call_api_delay,
            name="call_delay_api",
            args=()
        )
        thread_process.start()
        movie.status = StatusEnum.enabled.value
        movie.save()
        return True
    
    # Deleay Gateway
    class DelayGateway:

        def __init__(self, delay_time: int = 6000):
            self.delay_time = delay_time

        def call_api_delay(self):
            resp = get(f"{DELAY_API_URL}/{self.delay_time}/",
                    allow_redirects=False)
            print(
                f"Background process excuted correclty after {self.delay_time} ms")
            return True
    
    ```

4. **The endpoint that lists the movies by default filters the ones that are in draft status, and with a parameter includes them (document the solution) ✅**

    **Explanation:**

    The controller receive a queryparam "status" that by default is "enabled", and pass a filter object to the service in order to filter the model

    ```python
    # Movie Controller
    class MovieController(IsAuthController):
        def list_movies(self, request):
            service = MovieService()
            filters = {"status": request.GET.get("status", StatusEnum.enabled.value)}
            movies = service.list_movies(filters=filters)
            return Response(movies, status=status.HTTP_200_OK)

    # Movie Service method called by the controller
    class MovieService:
        
        def __init__(self) -> None:
            self.repo = MovieRepository()

        def list_movies(self, filters: dict = None):
            movies = self.repo.list(filters=filters)
            serializer = MoviePublicSerializer(movies, many=True)
            return serializer.data

    # Movie Repository called by the service
    class MovieRepository(BaseRepository):
        
        def __init__(self) -> None:
            self.repo = MovieRepository()

        def list(self, filters: dict = None):
            if filters is None:
                filters = {}
            return Movie.objects.filter(**filters)
    ```

5. ~~The movies created in draft state will only be available during that day, since every night a scheduled task will be run that will delete the movies that are still in draft state.~~ ❌
6. ~~Implement the solution with Celery~~ ❌

# Deliverables

1. **The source code must be submitted to a shared repository (Gitlab, Github or similar). ✅**
2. **The list of available endpoints and supported methods documented (could be in the same Github repo). ✅**
3. **Postman collection to play with your solution. ✅** ([see](/MOVIES.postman_collection.json))
4. **List of used libraries/frameworks. ✅**
5. **README file with the steps to run/setup the application ✅**

# Extra Credit

1. ~~Tests~~ ❌
2. ~~Docker, docker-compose.yml, seeds and README file to run it locally.~~ ❌
3. **Justification of chosen libraries/frameworks against other popular choices.** ✅([see](../README.md#tools-🛠️))
