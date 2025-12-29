# tests/test_natural_gas_new_methods.py
from __future__ import annotations

import pytest

# Update this import path to match your project structure.
# Example options:
#   from eia_python.source.natural_gas import NaturalGas
#   from eia_python.sources.natural_gas import NaturalGas
from eia_python.sources.natural_gas import NaturalGas


@pytest.fixture
def ng():
    """
    Instantiate NaturalGas without relying on its __init__ signature.
    We stub the instance methods used by the public API methods.
    """
    obj = NaturalGas.__new__(NaturalGas)
    return obj


def _install_spies(monkeypatch, ng, *, fetch_return=None, series_return=None):
    """
    Replace _fetch_data and get_series to:
    - capture call arguments (so we can assert correctness)
    - return deterministic outputs
    """
    calls = {}

    if fetch_return is None:
        fetch_return = {"raw": "payload"}

    if series_return is None:
        series_return = [{"period": "2020-01", "value": 1.0}]

    def _fetch_data(*, start, endpoint, series, frequency, offset=0, length=5000):
        calls["fetch"] = {
            "start": start,
            "endpoint": endpoint,
            "series": series,
            "frequency": frequency,
            "offset": offset,
            "length": length,
        }
        return fetch_return

    def get_series(payload):
        calls["series_payload"] = payload
        return series_return

    monkeypatch.setattr(ng, "_fetch_data", _fetch_data, raising=False)
    monkeypatch.setattr(ng, "get_series", get_series, raising=False)

    return calls, series_return


def test_storage_default_region_lower48(monkeypatch, ng):
    ng._STORAGE_SERIES_BY_REGION = {"lower48": "NW2_EPG0_SWO_R48_BCF"}  # example

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.storage(start="2020-01-01")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "stor/wkly/data/"
    assert calls["fetch"]["series"] == "NW2_EPG0_SWO_R48_BCF"
    assert calls["fetch"]["frequency"] == "weekly"
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


def test_storage_invalid_region_raises_valueerror(monkeypatch, ng):
    ng._STORAGE_SERIES_BY_REGION = {"lower48": "X", "east": "Y"}

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.storage(start="2020-01-01", region="bad_region")

    msg = str(e.value)
    assert "Invalid region='bad_region'" in msg
    assert "Valid:" in msg
    assert "lower48" in msg
    assert "east" in msg
    assert "or 'all'." in msg


def test_spot_prices_calls_correct_endpoint_and_series(monkeypatch, ng):
    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.spot_prices(start="2020-01-01", frequency="daily")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "pri/fut/data/s"
    assert calls["fetch"]["series"] == "RNGWHHD"
    assert calls["fetch"]["frequency"] == "daily"


def test_production_default_united_states_total(monkeypatch, ng):
    ng._PRODUCTION_SERIES_BY_STATE = {
        "united_states_total": "N9070US2",
        "tx": "NA1160_STX_2",
    }

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.production(start="2020-01", state="united_states_total")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "sum/snd/data/"
    assert calls["fetch"]["series"] == "N9070US2"
    assert calls["fetch"]["frequency"] == "monthly"


def test_production_state_tx(monkeypatch, ng):
    ng._PRODUCTION_SERIES_BY_STATE = {
        "united_states_total": "N9070US2",
        "tx": "NA1160_STX_2",
    }

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.production(start="2020-01", state="tx", offset=10, length=123)
    assert out == expected

    assert calls["fetch"]["series"] == "NA1160_STX_2"
    assert calls["fetch"]["offset"] == 10
    assert calls["fetch"]["length"] == 123


def test_consumption_default_united_states_total(monkeypatch, ng):
    ng._CONSUMPTION_SERIES_BY_STATE = {
        "united_states_total": "N9140US2",
        "tx": "N9140TX2",
    }

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.consumption(start="2020-01", state="united_states_total")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "sum/snd/data/"
    assert calls["fetch"]["series"] == "N9140US2"
    assert calls["fetch"]["frequency"] == "monthly"


def test_imports_default_united_states_pipeline_total(monkeypatch, ng):
    ng._IMPORT_SERIES_BY_COUNTRY = {
        "united_states_pipeline_total": "N9102US2",
        "canada_pipeline": "N9102CN2",
    }

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.imports(start="2020-01", country="united_states_pipeline_total")
    assert out == expected

    assert calls["fetch"]["endpoint"] == "sum/snd/data/"
    assert calls["fetch"]["series"] == "N9102US2"
    assert calls["fetch"]["frequency"] == "monthly"


def test_imports_invalid_country_raises_valueerror(monkeypatch, ng):
    ng._IMPORT_SERIES_BY_COUNTRY = {"united_states_pipeline_total": "N9102US2"}

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.imports(start="2020-01", country="bad_country")

    assert "Unsupported export destination" in str(e.value)
    assert "bad_country" in str(e.value)


def test_exports_default_united_states_pipeline_total(monkeypatch, ng):
    ng._EXPORT_SERIES_BY_COUNTRY = {
        "united_states_pipeline_total": "N9132US2",
        "mexico_pipeline": "N9132MX2",
    }

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.exports(
        start="2020-01", country="united_states_pipeline_total", offset=7, length=77
    )
    assert out == expected

    assert calls["fetch"]["endpoint"] == "sum/snd/data/"
    assert calls["fetch"]["series"] == "N9132US2"
    assert calls["fetch"]["frequency"] == "monthly"
    assert calls["fetch"]["offset"] == 7
    assert calls["fetch"]["length"] == 77


def test_exports_invalid_country_raises_valueerror(monkeypatch, ng):
    ng._EXPORT_SERIES_BY_COUNTRY = {"united_states_pipeline_total": "N9132US2"}

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.exports(start="2020-01", country="bad_country")

    assert "Unsupported export destination" in str(e.value)
    assert "bad_country" in str(e.value)


def test_futures_prices_default_contract_1(monkeypatch, ng):
    ng._FUTURES_SERIES_BY_CONTRACT = {1: "RNGC1", 2: "RNGC2"}

    calls, expected = _install_spies(monkeypatch, ng)

    out = ng.futures_prices(start="2020-01-01", contract=1)
    assert out == expected

    assert calls["fetch"]["endpoint"] == "pri/fut/data/"
    assert calls["fetch"]["series"] == "RNGC1"
    assert calls["fetch"]["frequency"] == "daily"
    # futures_prices ignores offset/length in your implementation
    assert calls["fetch"]["offset"] == 0
    assert calls["fetch"]["length"] == 5000


def test_futures_prices_invalid_contract_raises_valueerror(monkeypatch, ng):
    ng._FUTURES_SERIES_BY_CONTRACT = {1: "RNGC1"}

    _install_spies(monkeypatch, ng)

    with pytest.raises(ValueError) as e:
        ng.futures_prices(start="2020-01-01", contract=99)

    assert "Unsupported futures contract" in str(e.value)
    assert "99" in str(e.value)
