import os, yaml

def load_config():
    env = os.getenv("TEST_ENV", "test")  # default to 'test'
    path = os.path.join("config", f"{env}.yaml")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found for env={env}: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
