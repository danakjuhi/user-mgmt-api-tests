import pytest
from common.assertions import assert_code, assert_api_code

@pytest.mark.regression
def test_create_get_update_delete_user(users_api, random_user_payload, ensure_cleanup):
    # Create
    resp = users_api.create_user(random_user_payload)
    assert_code(resp, 200)
    body = resp.json()
    assert_api_code(body, 200)
    uid = body["data"]["id"]
    ensure_cleanup.add_user(uid)

    # Get
    r2 = users_api.get_user(uid)
    assert_code(r2, 200)
    b2 = r2.json()
    assert_api_code(b2, 200)
    assert b2["data"]["username"] == random_user_payload["username"]
    assert b2["data"]["email"] == random_user_payload["email"]

    # Update email
    new_email = "new_" + random_user_payload["email"]
    r3 = users_api.update_user_email(uid, new_email)
    assert_code(r3, 200)
    assert_api_code(r3.json(), 200)

    # Get confirm
    r4 = users_api.get_user(uid)
    assert_code(r4, 200)
    b4 = r4.json()
    assert_api_code(b4, 200)
    assert b4["data"]["email"] == new_email

    # Delete
    r5 = users_api.delete_user(uid)
    assert_code(r5, 200)
    assert_api_code(r5.json(), 200)
