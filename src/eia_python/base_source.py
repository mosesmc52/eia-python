from abc import ABC, abstractmethod
from typing import Any


class BaseSource(ABC):
    def __init__(self, client, base_endpoint):
        self.client = client
        self.base_endpoint = base_endpoint.rstrip("/") + "/"

    def _fetch_data(
        self,
        *,
        start: str,
        endpoint: str,
        series: str,
        frequency: str,
        offset: int = 0,
        length: int = 5000,
        direction: str = "desc",
        extra_params: dict | None = None,
    ) -> dict:
        full_endpoint = f"{self.base_endpoint}{endpoint.lstrip('/')}"
        return self.client._fetch(
            start=start,
            endpoint=full_endpoint,
            series=series,
            frequency=frequency,
            offset=offset,
            length=length,
            direction=direction,
            extra_params=extra_params,
        )

    def get_series(self, payload: dict) -> list[dict[str, Any]]:
        """
        EIA v2 typically returns data at payload['response']['data'].
        Centralizing this keeps source methods thin.
        """
        return (payload.get("response") or {}).get("data") or []

    @abstractmethod
    def imports(self):
        pass

    @abstractmethod
    def exports(self):
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
    def futures_prices(self):
        pass

    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def processing(self):
        pass
