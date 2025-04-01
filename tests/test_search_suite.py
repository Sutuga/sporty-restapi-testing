import pytest
from pytest_schema.helpers import exact
from resources import rest_api_helper as rah
from resources.resp_schema import common_response_schema


@pytest.mark.parametrize("endpoint,", ("author", "title"))
def test_01_test_verify_basic_response_for_valid_query(endpoint):
    """
    Validate the basic response for a valid query.
    """
    resp = rah.positive_request(endpoint, method="get")
    assert all(endpoint + "s" in r for r in resp), f"Expected {endpoint}s in response"
    print(resp)


@pytest.mark.parametrize(
    "data",
    [
        {"title": "Ozymandias"},
        {"author": "Matthew Prior"},
        {"title": "Mother"},
        {"author": "Julia Ward Howe", "title": "Mother"},
        {"author": "Jonathan Swift"},
    ],
)
def test_02_verify_response_for_valid_query(data):
    """
    Verify the response for a valid query. Mixing title and author in the same query.
    """
    endpoint = "/".join(f"{k}/{v}" for k, v in data.items())
    resp = rah.positive_request(endpoint, method="get")
    for result in resp:
        assert all(result[k] == v for k, v in data.items())


def test_03_empty_response_for_unknown_author():
    """
    Validate the response for an unknown author.
    """
    resp = rah.positive_request("author/UnknownAuthor", method="get")
    assert resp == {
        "reason": "Not found",
        "status": 404,
    }, "Empty response for unknown author"


def test_04_response_schema_validation():
    """
    Validate the response schema.
    """
    resp = rah.positive_request("random", method="get")
    assert all(
        exact(common_response_schema) == r for r in resp
    ), "Response schema does not match"
    print(resp)
