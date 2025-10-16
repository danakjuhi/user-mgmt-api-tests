from pydantic import BaseModel
from typing import Optional

class SuccessEnvelope(BaseModel):
    code: int
    data: dict | list | None
    msg: str

def test_success_envelope_shape(users_api):
    r = users_api.list_users(page=1, size=1)
    body = r.json()
    model = SuccessEnvelope(**body)
    assert model.code == 200
