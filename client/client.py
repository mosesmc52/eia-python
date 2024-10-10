import os
import textwrap


class EIAClient(object):
    def __init__(self, api_key: str, version: int):

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

        self.oil = None

    def _fetch(self, endpoint):
        pass

    def _parse(self, raw_data):
        pass
