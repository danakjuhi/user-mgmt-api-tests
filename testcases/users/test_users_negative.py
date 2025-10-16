import pytest
from common.assertions import assert_code

@pytest.mark.negative
def test_create_user_missing_fields(users_api):
    # missing email
    resp = users_api.create_user({"username": "x", "password": "Passw0rd!"})
    assert resp.status_code in (400, 422)

@pytest.mark.negative
def test_get_user_nonexistent(users_api):
    resp = users_api.get_user(99999999)
    assert resp.status_code in (404, 400)

@pytest.mark.negative
def test_update_email_invalid_format(users_api, random_user_payload):
    # First create a valid user to update
    c = users_api.create_user(random_user_payload)
    if c.status_code == 200:
        uid = c.json()["data"]["id"]
        r = users_api.update_user_email(uid, "not-an-email")
        assert r.status_code in (400, 422)

@pytest.mark.negative
def test_delete_user_twice(users_api, random_user_payload):
    # create then delete twice
    c = users_api.create_user(random_user_payload)
    if c.status_code == 200:
        uid = c.json()["data"]["id"]
        d1 = users_api.delete_user(uid)
        # second delete should error
        d2 = users_api.delete_user(uid)
        assert d2.status_code in (404, 400)

@pytest.mark.negative
def test_list_users_pagination_out_of_range(users_api):
    r = users_api.list_users(page=999999, size=10)
    # Could be 200 with empty list or 400 depending on service
    assert r.status_code in (200, 400)
