import allure

def assert_code(resp, expected: int = 200):
    with allure.step(f"Assert HTTP code == {expected}"):
        assert resp.status_code == expected, f"Expected {expected}, got {resp.status_code}: {getattr(resp, 'text', '')}"

def assert_api_code(body: dict, expected: int = 200):
    with allure.step(f"Assert API 'code' == {expected}"):
        assert body.get("code") == expected, f"Expected code {expected}, got {body}"
