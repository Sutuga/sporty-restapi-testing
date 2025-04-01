import requests
from resources import global_variables as gl


def send_test_request(method, url, params=None, headers=None, json=None):
    """
    Send a test request to the specified URL using the specified method and parameters.
    """
    session = requests.Session()
    resp = session.request(
        method,
        url,
        params=params or {},
        json=json or {},
        headers=headers or {},
        verify=True,
        timeout=10,
    )
    return resp


def positive_request(end_point, method="post", params=None, headers=None, json=None):
    """
    Send a request to the specified URL using the specified method and parameters.
    """
    url = gl.URL + end_point
    resp: requests.Response = send_test_request(method, url, params, headers, json)
    assert (
        resp.status_code == 200
    ), f"Request failed with status code {resp.status_code}, response: {resp.text}"
    assert (
        resp.elapsed.total_seconds() < 1
    ), f"Request took too long: {resp.elapsed.total_seconds()} seconds"
    return resp.json()
