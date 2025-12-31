# tests/test_electricity_generation.py
from __future__ import annotations

from typing import Any, Dict, List

import pytest

# Update this import path to match your package structure.
# Example:
#   from eia_ng.sources.electricity import Electricity
from eia_ng.sources.electricity import Electricity


@pytest.fixture
def elec():
    """
    Instantiate Electricity without relying on its __init__ signature.
    We stub the instance methods used by generation() and generation_natural_gas().
    """
    obj = Electricity.__new__(Electricity)
    return obj


def _install_spies(monkeypatch, elec, *, fetch_return=None, series_return=None):
    """
    Replace _fetch_v2 and get_series to:
      - capture call arguments for assertions
      - return deterministic values
    """
    calls: Dict[str, Any] = {}

    if fetch_return is None:
        fetch_return = {
            "response": {"data": [{"period": "2020-01", "generation": 123}]}
        }
    if series_return is None:
        series_return = [{"period": "2020-01", "generation": 123}]

    def _fetch_v2(
        *,
        start: str,
        endpoint: str,
        frequency: str,
        data_fields: List[str] | None = None,  # type: ignore[valid-type]
        facets: Dict[str, List[str]] | None = None,  # type: ignore[valid-type]
        offset: int = 0,
        length: int = 5000,
        direction: str = "desc",
        extra_params: Dict[str, Any] | None = None,  # type: ignore[valid-type]
    ) -> dict:
        calls["fetch"] = {
            "start": start,
            "endpoint": endpoint,
            "frequency": frequency,
            "data_fields": data_fields,
            "facets": facets,
            "offset": offset,
            "length": length,
            "direction": direction,
            "extra_params": extra_params,
        }
        return fetch_return

    def get_series(payload: dict) -> List[Dict[str, Any]]:
        calls["series_payload"] = payload
        return series_return

    monkeypatch.setattr(elec, "_fetch_v2", _fetch_v2, raising=False)
    monkeypatch.setattr(elec, "get_series", get_series, raising=False)

    return calls, series_return


def test_generation_defaults_to_us_natural_gas(monkeypatch, elec):
    calls, expected = _install_spies(monkeypatch, elec)

    out = elec.generation(start="2020-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "electric-power-operational-data/data/"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["data_fields"] == ["generation"]

    facets = calls["fetch"]["facets"]
    assert facets["fueltypeid"] == ["NG"]
    assert facets["location"] == ["US"]
    assert facets["sectorid"] == ["99"]


def test_generation_multiple_locations_single_request(monkeypatch, elec):
    calls, expected = _install_spies(monkeypatch, elec)

    out = elec.generation(
        start="2020-01",
        fueltypeid="NG",
        locations=["US", "UT"],
        sectorid="99",
        frequency="monthly",
        offset=10,
        length=123,
    )
    assert out == expected

    facets = calls["fetch"]["facets"]
    assert facets["fueltypeid"] == ["NG"]
    assert facets["location"] == ["US", "UT"]
    assert facets["sectorid"] == ["99"]

    assert calls["fetch"]["offset"] == 10
    assert calls["fetch"]["length"] == 123


def test_generation_non_default_fuel(monkeypatch, elec):
    calls, expected = _install_spies(monkeypatch, elec)

    out = elec.generation(start="2020-01", fueltypeid="COL", locations=["US"])
    assert out == expected

    facets = calls["fetch"]["facets"]
    assert facets["fueltypeid"] == ["COL"]
    assert facets["location"] == ["US"]


def test_generation_natural_gas_us_total(monkeypatch, elec):
    calls, expected = _install_spies(monkeypatch, elec)

    out = elec.generation_natural_gas(start="2020-01", state=None)
    assert out == expected

    facets = calls["fetch"]["facets"]
    assert facets["fueltypeid"] == ["NG"]
    assert facets["location"] == ["US"]
    assert facets["sectorid"] == ["99"]


def test_generation_natural_gas_state_uppercases(monkeypatch, elec):
    calls, expected = _install_spies(monkeypatch, elec)

    out = elec.generation_natural_gas(start="2020-01", state="ut")
    assert out == expected

    facets = calls["fetch"]["facets"]
    assert facets["fueltypeid"] == ["NG"]
    assert facets["location"] == ["UT"]
    assert facets["sectorid"] == ["99"]
