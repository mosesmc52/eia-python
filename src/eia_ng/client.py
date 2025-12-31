import os
import textwrap
from typing import Any, Dict, Optional

from .helpers import retry_request
from .sources.electricity import Electricity
from .sources.natural_gas import NaturalGas


class EIAClient(object):
    def __init__(self, api_key: str = None, version: int = 2):

        self.api_key = None
        if api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = os.environ.get("EIA_API_KEY")

        if self.api_key is None:

            raise ValueError(
                textwrap.dedent(
                    """\
                    You need to set a valid API key. You can set it in 2 ways:
                    pass the string with api_key, or set api_key_file to a
                    file with the api key in the first line, or set the
                    environment variable 'EIA_API_KEY' to the value of your
                    api key. You can sign up for a free api key on the Fred
                    website at https://www.eia.gov/opendata/register.php/"""
                )
            )

        self.host = "api.eia.gov"
        self.version = version
        self.natural_gas = NaturalGas(self)
        self.electricity = Electricity(self)

    def _fetch(
        self,
        start,
        endpoint,
        series,
        frequency="daily",
        offset=0,
        length=5000,
        direction="desc",
        extra_params: Optional[Dict[str, Any]] = None,
    ):
        params = {
            "api_key": self.api_key,
            "frequency": frequency,
            "facets[series][]": series,
            "start": start,
            "sort[0][column]": "period",
            "sort[0][direction]": direction,
            "offset": offset,
            "length": length,
        }

        if extra_params:
            params.update(extra_params)

        url = f"https://{self.host}/v{self.version}/{endpoint.lstrip('/')}"

        r = retry_request(url=url, params=params)
        return r.json()
