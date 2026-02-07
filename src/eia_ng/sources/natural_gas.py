from typing import Any

from ..datasets.natural_gas_series import (
    CONSUMPTION_SERIES_BY_STATE,
    EXPORT_SERIES_BY_COUNTRY,
    FUTURES_SERIES_BY_CONTRACT,
    IMPORT_SERIES_BY_COUNTRY,
    NG_EFP_DRY_BY_STATE,
    NG_PROVED_WET_ASSOC_BY_STATE,
    NG_PROVED_WET_NONASSOC_BY_STATE,
    NGL_PROVED_BY_STATE,
    PRODUCTION_SERIES_BY_STATE,
    STORAGE_SERIES_BY_REGION,
)
from .base import BaseSource


class NaturalGas(BaseSource):
    def __init__(self, client):
        super().__init__(client, base_endpoint="natural-gas/")

    def storage(
        self,
        start: str,
        end: str = None,
        region: str = "lower48",
        frequency: str = "weekly",
        offset: int = 0,
        length: int = 5000,
    ) -> Any:
        endpoint = "stor/wkly/data/"

        try:
            series = STORAGE_SERIES_BY_REGION[region]
        except KeyError as e:
            valid = ", ".join(sorted(STORAGE_SERIES_BY_REGION.keys()))
            raise ValueError(
                f"Invalid region='{region}'. Valid: {valid}, or 'all'."
            ) from e

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def spot_prices(
        self,
        start: str,
        end: str = None,
        frequency: str = "daily",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "pri/fut/data/"
        series = "RNGWHHD"
        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
        )
        return self.get_series(payload)

    def production(
        self,
        start: str,
        end: str = None,
        state: str = "united_states_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "sum/snd/data/"

        series = PRODUCTION_SERIES_BY_STATE[state]

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def consumption(
        self,
        start: str,
        end: str = None,
        state: str = "united_states_total",
        frequency: str = "monthly",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "sum/snd/data/"
        series = CONSUMPTION_SERIES_BY_STATE[state]

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def imports(
        self,
        start: str,
        end: str = None,
        frequency: str = "monthly",
        country: str = "united_states_pipeline_total",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "move/impc/data/"
        try:
            series = IMPORT_SERIES_BY_COUNTRY[country]
        except KeyError:
            raise ValueError(f"Unsupported export destination: {country}")

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def exports(
        self,
        start: str,
        end: str = None,
        frequency: str = "monthly",
        country: str = "united_states_pipeline_total",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "move/expc/data/"
        try:
            series = EXPORT_SERIES_BY_COUNTRY[country]
        except KeyError:
            raise ValueError(f"Unsupported export destination: {country}")

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            frequency=frequency,
            data_fields=["value"],
            offset=offset,
            length=length,
        )
        return self.get_series(payload)

    def futures_prices(
        self,
        start: str = None,
        end: str = None,
        contract: int = 1,
        frequency: str = "daily",
        offset: int = 0,
        length: int = 5000,
    ):
        endpoint = "pri/fut/data/"
        try:
            series = FUTURES_SERIES_BY_CONTRACT[contract]
        except KeyError:
            raise ValueError(f"Unsupported futures contract: {contract}")

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            data_fields=["value"],
            frequency=frequency,
        )
        return self.get_series(payload)

    def exploration_and_reserves(
        self,
        start: str = None,
        end: str = None,
        frequency: str = "annual",  # locked default
        offset: int = 0,
        length: int = 5000,
        state: str = "all",
        resource_category: str = "proved_associated_gas",
    ):
        """
        Fetch EIA Exploration & Reserves (ENR) data.
        NOTE: ENR data is annual only.
        """

        if frequency != "annual":
            raise ValueError(
                f"Invalid frequency='{frequency}'. "
                "Exploration & Reserves data is annual only."
            )

        endpoint = "enr/sum/data/"

        st = (state or "all").strip().lower()

        category_map = {
            "proved_associated_gas": NG_PROVED_WET_ASSOC_BY_STATE,
            "proved_nonassociated_gas": NG_PROVED_WET_NONASSOC_BY_STATE,
            "proved_ngl": NGL_PROVED_BY_STATE,
            "expected_future_gas_production": NG_EFP_DRY_BY_STATE,
        }

        if resource_category not in category_map:
            raise ValueError(
                f"Unsupported resource category: {resource_category}. "
                f"Valid: {sorted(category_map.keys())}"
            )

        series_map = category_map[resource_category]

        try:
            series = series_map[st]
        except KeyError as e:
            raise KeyError(
                f"Unknown state '{state}' (normalized '{st}'). "
                "Expected 2-letter state code or 'us'/'all'."
            ) from e

        payload = self._fetch_v2(
            start=start,
            end=end,
            endpoint=endpoint,
            series=series,
            data_fields=["value"],
            frequency="annual",
            offset=offset,
            length=length,
        )
        return self.get_series(payload)
