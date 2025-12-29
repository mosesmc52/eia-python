from typing import Any, Dict

from ..base_source import BaseSource


class NaturalGas(BaseSource):
    def __init__(self, client):
        super().__init__(client, base_endpoint="natural-gas/")

    _STORAGE_SERIES_BY_REGION: Dict[str, str] = {
        # examples only — replace with your actual EIA series codes
        "lower48": "NW2_EPG0_SWO_R48_BCF",
        "east": "NW2_EPG0_SWO_R31_BCF",
        "midwest": "NW2_EPG0_SWO_R32_BCF",
        "south_central": "NW2_EPG0_SWO_R33_BCF",
        "mountain": "NW2_EPG0_SWO_R34_BCF",
        "pacific": "NW2_EPG0_SWO_R35_BCF",
    }

    def storage(
        self,
        start: str,
        region: str = "lower48",
        frequency: str = "weekly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        endpoint = "stor/wkly/data/"

        if region == "all":
            out: Dict[str, Any] = {}
            for reg, series in self._STORAGE_SERIES_BY_REGION.items():
                payload = self._fetch_data(
                    start=start,
                    endpoint=endpoint,
                    series=series,
                    frequency=frequency,
                    offset=offset,
                    length=length,
                )
                out[reg] = self.get_series(payload)
            return out

        try:
            series = self._STORAGE_SERIES_BY_REGION[region]
        except KeyError as e:
            valid = ", ".join(sorted(self._STORAGE_SERIES_BY_REGION.keys()))
            raise ValueError(
                f"Invalid region='{region}'. Valid: {valid}, or 'all'."
            ) from e

        payload = self._fetch_data(
            start=start,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def spot_prices(self, start: str, frequency: str = "daily"):
        endpoint = "pri/fut/data/s"
        series = "RNGWHHD"
        payload = self._fetch_data(
            start=start,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
        )
        return self.get_series(payload)

    def production(self):
        raise NotImplementedError

    def reserves(self):
        raise NotImplementedError

    def imports(self):
        raise NotImplementedError

    def export(self):
        raise NotImplementedError

    def futures_price(self):
        raise NotImplementedError

    def consumption(self):
        raise NotImplementedError

    def processing(self):
        raise NotImplementedError

    def electricity_generation(self):
        raise NotImplementedError
