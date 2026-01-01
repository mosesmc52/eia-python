from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List

import pytest
from eia_ng import EIAClient


def _load_env_if_possible() -> None:
    """
    Load .env from the repo root if python-dotenv is installed.
    This keeps local developer experience smooth without forcing dotenv in prod usage.
    """
    try:
        from dotenv import load_dotenv  # type: ignore
    except Exception:
        return
    # Load .env from project root
    ROOT = Path(__file__).resolve().parents[1]
    # Load from current working directory (repo root in most cases)
    load_dotenv(ROOT / ".env")


def _require_api_key() -> str:
    _load_env_if_possible()
    api_key = os.getenv("EIA_API_KEY")
    if not api_key:
        pytest.skip(
            "EIA_API_KEY not set. Set it in env or .env to run integration smoke tests."
        )
    return api_key


def _assert_rows(rows: List[Dict[str, Any]], *, min_len: int = 1) -> None:
    assert isinstance(rows, list)
    assert len(rows) >= min_len
    assert isinstance(rows[0], dict)

    if "period" in rows[0]:
        assert rows[0]["period"] is None or isinstance(rows[0]["period"], str)


@pytest.mark.integration
def test_smoke_all_functions():
    """
    Integration smoke test: hits the real EIA API and ensures each public method returns rows.

    Run:
      EIA_API_KEY=... pytest -m integration -q
    """
    api_key = _require_api_key()

    client = EIAClient(api_key=api_key, version=2)

    # -----------------------------
    # Natural Gas
    # -----------------------------

    # Storage (weekly) - lower48 default
    storage = client.natural_gas.storage(start="2023-01-01", region="lower48", length=5)
    _assert_rows(storage)

    # Spot prices (daily) - Henry Hub
    spot = client.natural_gas.spot_prices(start="2023-01-01", frequency="daily")
    _assert_rows(spot)

    # Production (monthly) - U.S. total
    prod_us = client.natural_gas.production(
        start="2022-01",
        state="united_states_total",
        frequency="monthly",
        length=5,
    )
    _assert_rows(prod_us)

    # Consumption (monthly) - U.S. total
    cons_us = client.natural_gas.consumption(
        start="2022-01",
        state="united_states_total",
        frequency="monthly",
        length=5,
    )
    _assert_rows(cons_us)

    # Imports (monthly) - U.S. pipeline total
    imps = client.natural_gas.imports(
        start="2022-01",
        country="united_states_pipeline_total",
        frequency="monthly",
        length=5,
    )
    _assert_rows(imps)

    # Exports (monthly) - U.S. pipeline total
    exps = client.natural_gas.exports(
        start="2022-01",
        country="united_states_pipeline_total",
        length=5,
    )
    _assert_rows(exps)

    # Futures prices (daily) - contract 1
    fut = client.natural_gas.futures_prices(start="2023-01-01", contract=1)
    _assert_rows(fut)

    # -----------------------------
    # Electricity (Natural Gas generation)
    # -----------------------------

    gen_us = client.electricity.generation_natural_gas(
        start="2022-01", frequency="monthly"
    )
    _assert_rows(gen_us)

    # # Optional: state example (UT)
    gen_ut = client.electricity.generation_natural_gas(
        start="2022-01", state="UT", frequency="monthly"
    )
    _assert_rows(gen_ut)
