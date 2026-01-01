from __future__ import annotations

import random
import time
from typing import Any, Dict, Optional

import requests
from requests import Response
from requests.exceptions import RequestException

RETRYABLE_STATUS = {429, 500, 502, 503, 504}


def retry_request(
    *,
    url: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    max_retries: int = 5,
    backoff_factor: float = 1.5,
    timeout: int = 30,
) -> Response:
    """
    Return a requests.Response or raise RequestException after retries.

    Retries on network errors and retryable HTTP status codes.
    """
    headers = headers or {"accept": "application/json"}
    delay = 1.0
    last_exc: Optional[Exception] = None

    for attempt in range(1, max_retries + 1):
        try:
            r = requests.get(url, headers=headers, params=params, timeout=timeout)

            # Retry on known transient statuses
            if r.status_code in RETRYABLE_STATUS:
                last_exc = RequestException(
                    f"Retryable HTTP {r.status_code} on attempt {attempt}: {r.text[:200]}"
                )
            else:
                r.raise_for_status()
                return r

        except RequestException as e:
            last_exc = e

        # If final attempt, break and raise
        if attempt == max_retries:
            break

        # Exponential backoff with jitter
        sleep_for = delay * (backoff_factor ** (attempt - 1))
        sleep_for += random.uniform(0, 0.25 * sleep_for)
        time.sleep(sleep_for)

    # If we got here, everything failed
    assert last_exc is not None
    raise last_exc
