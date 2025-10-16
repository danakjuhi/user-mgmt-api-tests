# user-mgmt-api-tests

# User Management API — Automated Tests (Python + Pytest + Allure)

Portfolio-ready framework testing a hypothetical **User Management REST API**:
Create/Get/Update/Delete User and List Users, with positive and negative cases.

## Tech
- Python, pytest, requests, allure-pytest
- PyYAML for env configs, tenacity for retries, optional pydantic for schemas
- GitHub Actions CI, parallel runs with pytest-xdist

## Structure
testcases/ # tests split by module (smoke, users, contract)
api/ # API wrapper classes
common/ # config, logger, assertions, http client
config/ # env configs (test/stage/prod)
reports/ # Allure results & HTML reports (gitignored)
