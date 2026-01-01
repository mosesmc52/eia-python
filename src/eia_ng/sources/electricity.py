from __future__ import annotations

from typing import Any, Dict, List, Optional

from .base import BaseSource


class Electricity(BaseSource):
    """
    Electricity (EIA v2) convenience wrappers.
    """

    def __init__(self, client):
        super().__init__(client=client, base_endpoint="electricity/")

    def generation(
        self,
        start: str,
        frequency: str = "monthly",
        fueltypeid: str = "NG",
        locations: Optional[List[str]] = None,
        sectorid: str = "99",
        offset: int = 0,
        length: int = 5000,
    ) -> List[Dict[str, Any]]:
        """
        Net generation by fuel and location(s).

        locations:
          - ["US"] for national
          - ["UT"] for a single state
          - ["US", "UT"] to request multiple in one call (like your example)
        """
        if locations is None:
            locations = ["US"]

        payload = self._fetch_v2(
            start=start,
            endpoint="electric-power-operational-data/data/",
            frequency=frequency,
            data_fields=["generation"],
            facets={
                "fueltypeid": [fueltypeid],
                "location": locations,
                "sectorid": [sectorid],
            },
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def generation_natural_gas(
        self,
        start: str,
        frequency: str = "monthly",
        state: Optional[str] = None,
        sectorid: str = "99",
        offset: int = 0,
        length: int = 5000,
    ) -> List[Dict[str, Any]]:
        """
        Convenience wrapper: natural-gas-fired generation.

        state:
          - None => US total
          - "UT" => that state
        """
        locations = ["US"] if state is None else [state.upper()]
        return self.generation(
            start=start,
            frequency=frequency,
            fueltypeid="NG",
            locations=locations,
            sectorid=sectorid,
            offset=offset,
            length=length,
        )
