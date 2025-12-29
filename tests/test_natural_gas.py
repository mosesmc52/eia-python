from unittest.mock import Mock

import pytest
import requests
from eia_python import EIAClient


def _fake_eia_payload(series_id: str):
    # Mimic EIA v2 shape: payload["response"]["data"] is what get_series() reads
    return {
        "response": {
            "data": [
                {
                    "period": "2024-01-12",
                    "series": series_id,
                    "value": 100.0,
                    "units": "BCF",
                },
                {
                    "period": "2024-01-05",
                    "series": series_id,
                    "value": 95.0,
                    "units": "BCF",
                },
            ]
        }
    }


def _mock_requests_get_factory(expected_url_substring: str, expected_series_id: str):
    """
    Returns a function that can replace requests.get and will assert URL + params.
    """

    def _mock_get(url, headers=None, params=None, timeout=None):
        assert expected_url_substring in url, f"Unexpected URL: {url}"

        # Validate required params from your _fetch() builder
        assert params is not None
        assert params.get("api_key") == "TEST_KEY"
        assert params.get("facets[series][]") == expected_series_id
        assert "frequency" in params
        assert params.get("data[0]") == "value"
        assert params.get("sort[0][column]") == "period"

        # Mock response object
        resp = Mock()
        resp.raise_for_status = Mock()
        resp.json = Mock(return_value=_fake_eia_payload(expected_series_id))
        return resp

    return _mock_get


@pytest.fixture
def client(monkeypatch):
    # Ensure deterministic API key
    monkeypatch.setenv("EIA_API_KEY", "TEST_KEY")
    return EIAClient()


def test_storage_lower48_mocks_requests_get(client, monkeypatch):
    # Update these to match your NaturalGas mapping
    expected_series = "NW2_EPG0_SWO_R48_BCF"
    expected_url_part = "/v2/natural-gas/stor/wkly/data/"

    monkeypatch.setattr(
        requests,
        "get",
        _mock_requests_get_factory(expected_url_part, expected_series),
    )

    rows = client.natural_gas.storage(
        start="2024-01-01",
        region="lower48",
        frequency="weekly",
    )

    assert isinstance(rows, list)
    assert len(rows) == 2
    assert rows[0]["series"] == expected_series
    assert "period" in rows[0]
    assert "value" in rows[0]


def test_spot_prices_mocks_requests_get(client, monkeypatch):
    # Update these to match your NaturalGas.spot_prices() implementation
    expected_series = "RNGWHHD"
    expected_url_part = "/v2/natural-gas/pri/fut/data/s"

    monkeypatch.setattr(
        requests,
        "get",
        _mock_requests_get_factory(expected_url_part, expected_series),
    )

    rows = client.natural_gas.spot_prices(
        start="2024-01-01",
        frequency="daily",
    )

    assert isinstance(rows, list)
    assert len(rows) == 2
    assert rows[0]["series"] == expected_series
    assert "period" in rows[0]
    assert "value" in rows[0]


def test_storage_invalid_region_raises(client):
    with pytest.raises(ValueError):
        client.natural_gas.storage(
            start="2024-01-01",
            region="not_a_region",
        )
