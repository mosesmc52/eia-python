import time

import requests
from requests.exceptions import RequestException


def retry_request(
    url,
    max_retries=3,
    backoff_factor=2,
    params=None,
    headers={"accept": "application/json"},
):
    retries = 0
    retry_delay = 1

    while retries < max_retries:
        try:
            response = requests.get(url, headers=headers, params=params)
            # Check if the request was successful
            response.raise_for_status()
            return response
        except RequestException as e:
            print(f"Request failed: {str(e)}")

        retries += 1
        retry_delay *= backoff_factor
        time.sleep(retry_delay)

    # Max retries exceeded
    return None
