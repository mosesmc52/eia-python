from abc import ABC, abstractmethod


class BaseSource(ABC):
    def __init__(self, client):
        self.client = client

    @abstractmethod
    def transport(self):
        pass

    @abstractmethod
    def reserves(self):
        pass

    @abstractmethod
    def production(self):
        pass

    @abstractmethod
    def storage(self):
        pass

    @abstractmethod
    def spot_prices(self):
        pass

    @abstractmethod
    def futures_price(self):
        pass

    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def processing(self):
        pass

    @abstractmethod
    def electricity_generation(self):
        pass
