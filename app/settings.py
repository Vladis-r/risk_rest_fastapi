import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    # app
    app_name: str
    app_host: str
    app_port: int
    is_debug: bool

    # database
    sqla_db_url: str
    test_db_url: str
    model_config = SettingsConfigDict(env_file=f'{os.getcwd()}\\app\\.env', env_file_encoding='utf-8')


settings = AppSettings()
