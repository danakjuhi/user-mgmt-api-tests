import json
import allure
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

class HttpClient:
    def __init__(self, base_url: str, timeout: int = 10, retries: int = 2, token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.token = token
        self.retries = retries

    def _headers(self, headers: dict | None = None):
        base = {"Content-Type": "application/json"}
        if self.token:
            base["Authorization"] = f"Bearer {self.token}"
        if headers:
            base.update(headers)
        return base

    def _attach(self, method: str, url: str, **kwargs):
        allure.attach(json.dumps({"method": method, "url": url, "kwargs": kwargs}, indent=2),
                      name="request", attachment_type=allure.attachment_type.JSON)

    def _attach_response(self, resp: requests.Response):
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        allure.attach(json.dumps({
            "status_code": resp.status_code,
            "headers": dict(resp.headers),
            "body": body
        }, indent=2), name="response", attachment_type=allure.attachment_type.JSON)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}"
        kwargs.setdefault("timeout", self.timeout)
        kwargs["headers"] = self._headers(kwargs.get("headers"))
        self._attach(method, url, **kwargs)
        resp = self.session.request(method, url, **kwargs)
        self._attach_response(resp)
        return resp
