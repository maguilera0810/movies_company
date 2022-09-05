from django.contrib.auth.models import User
from django.db import models

from apps.core.models import DatedModel, StatusModel


class Genre(DatedModel):
    """
    Genre Model:

    - name (str)
    - code (slug)
    - created_at (datetime)
    - updated_at (datetime)

    """
    name = models.CharField(max_length=50)
    code = models.SlugField(max_length=60, null=True)

    def save(self, *args, **kwargs):
        adding = self._state.adding
        super(Genre, self).save(*args, **kwargs)
        if adding:
            self.code = f"genre-{self.id}"
            self.save()


class Movie(DatedModel, StatusModel):
    """
    Movie Model:

    - title (str)
    - code (slug)
    # - year_release (int)
    - release (date)
    - casting (User[])
    - producers (User[])
    - directors (User[])
    - genres (Genre[])
    - created_at (datetime)
    - updated_at (datetime)

    """
    title = models.CharField(max_length=50, null=False, blank=False)
    code = models.SlugField(max_length=60, null=True)
    release = models.DateField()
    casting = models.ManyToManyField(User, related_name='movie_casting')
    producers = models.ManyToManyField(User, related_name='movie_producers')
    directors = models.ManyToManyField(User, related_name='movie_directors')
    genres = models.ManyToManyField(Genre, related_name='movie_genre',
                                    null=False, blank=False)

    def save(self, *args, **kwargs):
        adding = self._state.adding
        super(Movie, self).save(*args, **kwargs)
        if adding:
            self.code = f"movie-{self.id}"
            self.save()
