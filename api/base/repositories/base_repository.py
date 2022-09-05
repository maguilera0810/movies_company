from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def list(self, filters: dict = None):
        pass

    @abstractmethod
    def delete(self, id):
        pass
