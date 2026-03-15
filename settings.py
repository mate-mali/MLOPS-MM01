from pydantic_settings import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str):
        if value in ("dev", "prod", "test"):
            return value
        else:
            raise ValueError("ENVIRONMENT must be one of 'dev', 'prod', or 'test'")
