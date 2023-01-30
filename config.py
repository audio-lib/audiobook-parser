import os


class AppConfig:

    def __init__(self, api_id: str, api_hash: str, username: str, phone: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.username = username
        self.phone = phone


def get_config() -> AppConfig:
    api_id = os.getenv('api_id')
    api_hash = os.getenv('api_hash')
    username = os.getenv('username')
    phone = os.getenv('phone')
    return AppConfig(api_id, api_hash, username, phone)
