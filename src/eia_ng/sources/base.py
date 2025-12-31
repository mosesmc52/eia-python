from abc import ABC
from typing import Any, Dict, List, Optional, abstractmethod


class BaseSource(ABC):
    def __init__(self, client, base_endpoint):
        self.client = client
        self.base_endpoint = base_endpoint.rstrip("/") + "/"

    def _fetch_v2(
        self,
        *,
        start: str,
        endpoint: str,
        frequency: str,
        data_fields: Optional[List[str]] = None,
        facets: Optional[Dict[str, List[str]]] = None,
        offset: int = 0,
        length: int = 5000,
        direction: str = "desc",
        extra_params: Optional[Dict[str, Any]] = None,
    ) -> dict:

        full_endpoint = f"{self.base_endpoint}{endpoint.lstrip('/')}"

        params: Dict[str, Any] = {}
        if data_fields:
            for i, f in enumerate(data_fields):
                params[f"data[{i}]"] = f

        if facets:
            for facet_name, values in facets.items():
                # allow a single string to be passed accidentally
                if isinstance(values, str):  # type: ignore
                    values = [values]  # type: ignore
                params[f"facets[{facet_name}][]"] = values

        if extra_params:
            params.update(extra_params)

        return self.client._fetch(
            start=start,
            endpoint=full_endpoint,
            frequency=frequency,
            offset=offset,
            length=length,
            direction=direction,
            extra_params=params,
        )

    def get_series(self, payload: dict) -> list[dict[str, Any]]:
        """
        EIA v2 typically returns data at payload['response']['data'].
        Centralizing this keeps source methods thin.
        """
        return (payload.get("response") or {}).get("data") or []
