# eia-ng
A Python client for the EIA v2 natural gas API with structured access to production, storage, consumption, imports, exports, prices, and natural-gas-fired electricity generation.

## EIA API Documentation

This library is built on top of the official U.S. Energy Information Administration
(EIA) Open Data API.

For detailed information about datasets, endpoints, parameters, and data definitions,
refer to the official EIA API documentation:

https://www.eia.gov/opendata/documentation.php

## Installation

```bash
pip install eia-ng-client
```

## 3. API key setup

You need a free EIA API key.

1. Register at: https://www.eia.gov/opendata/register.php
2. Set the key as an environment variable:

```bash
export EIA_API_KEY="your_api_key_here"
```
---
## 4. Quick start

```python
from eia_ng import EIAClient

client = EIAClient()

# U.S. natural gas production (monthly)
production = client.natural_gas.production(start="2020-01")
print(production[:3])

# Lower 48 natural gas storage (weekly)
storage = client.natural_gas.storage(start="2022-01-01")
print(storage[:3])

# Henry Hub spot prices (daily)
prices = client.natural_gas.spot_prices(start="2023-01-01")
print(prices[:3])
```
---
## 5. Natural gas API overview

### Natural Gas Data

The `natural_gas` source provides access to:

- Production (U.S. total and by state)
- Consumption (U.S. total and by state)
- Storage (by region)
- Imports (pipeline, LNG, compressed)
- Exports (pipeline, LNG, truck, compressed)
- Spot prices (Henry Hub)
- Futures prices (front-month and deferred contracts)

#### Production by State

```python
# Texas natural gas production
tx_prod = client.natural_gas.production(
    start="2020-01",
    state="tx",
)
```


#### Storage by region


```python
# Lower 48 storage
storage = client.natural_gas.storage(
    start="2022-01-01",
    region="lower48",
)
```


#### Imports / exports



```python
# Pipeline imports from Canada
imports = client.natural_gas.imports(
    start="2021-01",
    country="canada_pipeline",
)

# Pipeline exports to Mexico
exports = client.natural_gas.exports(
    start="2021-01",
    country="mexico_pipeline",
)
```


#### Futures prices

```python
# Front-month natural gas futures
futures = client.natural_gas.futures_prices(
    start="2023-01-01",
    contract=1,
)
```

### Exploration & Reserves (Annual)

The `exploration_and_reserves` method provides access to EIA **Exploration & Reserves**
(Form-23) data. This data is **annual only** and represents reserve stocks or expected
future production, not current output.

Supported categories:

- Proved associated natural gas reserves (wet)
- Proved nonassociated natural gas reserves (wet)
- Proved natural gas plant liquids (NGL) reserves
- Expected future production of dry natural gas

#### Proved associated natural gas reserves

```python
# U.S. total proved associated natural gas reserves (annual)
reserves_us = client.natural_gas.exploration_and_reserves(
    start="2010",
    resource_category="proved_associated_gas",
)
print(reserves_us[:3])

# Texas proved associated natural gas reserves
reserves_tx = client.natural_gas.exploration_and_reserves(
    start="2010",
    state="tx",
    resource_category="proved_associated_gas",
)
print(reserves_tx[:3])

# Pennsylvania proved nonassociated gas reserves
pa_nonassoc = client.natural_gas.exploration_and_reserves(
    start="2010",
    state="pa",
    resource_category="proved_nonassociated_gas",
)


# U.S. proved NGL reserves
ngl_reserves = client.natural_gas.exploration_and_reserves(
    start="2010",
    resource_category="proved_ngl",
)

# Expected future production of dry natural gas (U.S.)
efp = client.natural_gas.exploration_and_reserves(
    start="2010",
    resource_category="expected_future_gas_production",
)
```



---

## 7. Electricity generation (Natural Gas)


```python
# U.S. electricity generation from natural gas
gen_us = client.electricity.generation_natural_gas(
    start="2020-01",
)

# Utah electricity generation from natural gas
gen_ut = client.electricity.generation_natural_gas(
    start="2020-01",
    state="UT",
)
```



## Returned Data Format

All methods return a list of dictionaries corresponding to rows returned by the EIA API.


You can easily convert the results to pandas using this approach.

```python
import pandas as pd
df = pd.DataFrame(production)

```

## License

MIT
