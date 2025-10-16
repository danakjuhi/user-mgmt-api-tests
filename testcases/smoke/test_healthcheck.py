import pytest
from common.assertions import assert_code, assert_api_code

@pytest.mark.smoke
def test_list_users_smoke(users_api):
    resp = users_api.list_users(page=1, size=1)
    assert_code(resp, 200)
    body = resp.json()
    assert_api_code(body, 200)
    # minimal structural checks (won't fail if list empty)
    assert "data" in body and "msg" in body
