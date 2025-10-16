import json
from common.http_client import HttpClient

class UsersAPI:
    def __init__(self, client: HttpClient):
        self.client = client

    def create_user(self, payload: dict):
        return self.client.request("POST", "/api/v1/users", data=json.dumps(payload))

    def get_user(self, user_id: int | str):
        return self.client.request("GET", f"/api/v1/users/{user_id}")

    def update_user_email(self, user_id: int | str, email: str):
        return self.client.request("PUT", f"/api/v1/users/{user_id}", data=json.dumps({"email": email}))

    def delete_user(self, user_id: int | str):
        return self.client.request("DELETE", f"/api/v1/users/{user_id}")

    def list_users(self, page=1, size=10, keyword=""):
        params = {"page": page, "size": size}
        if keyword:
            params["keyword"] = keyword
        return self.client.request("GET", "/api/v1/users", params=params)
