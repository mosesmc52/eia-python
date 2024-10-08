from abc import ABC, abstractmethod


class BaseSource(ABC):
    def __init__(self, client):
        self.client = client

    @abstractmethod
    def reserves(self):
        pass

    @abstractmethod
    def production(self):
        pass

    @abstractmethod
    def stocks(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def processing(self):
        pass

    @abstractmethod
    def generation(self):
        pass

    def _fetch(self, endpoint):
        pass

    def _parse(self, raw_data):
        pass
