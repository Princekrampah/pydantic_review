# Pydantic Settings
# poetry add pydantic-settings

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import (
    Field,
    PostgresDsn,
    RedisDsn
)
import os

# os.environ["API_KEY"] = "kkk222-111-44-666"
# os.environ["PG_DNS"] = "postgres://user:pass@localhost:5432/foobar"
# os.environ["REDIS_DNS"] = "redis://user:pass@localhost:6379/1"


# class Settings(BaseSettings):
#     api_key: str = Field(..., alias="api_key")
#     pg_dns: PostgresDsn
#     redis_dns: RedisDsn


# print(Settings().model_dump())


# This will load from a file, if and only if the OS env is not setup
# class Settings(BaseSettings):
#     api_key: str = Field(..., alias="api_key")
#     pg_dns: PostgresDsn
#     redis_dns: RedisDsn
#     model_config = SettingsConfigDict(
#         env_file=".env", env_file_encoding="utf-8")


# # first approach
# print(Settings().model_dump())


# # seconf approach
# print(Settings(_env_file=".env", _env_file_encoding="utf-8").model_dump())


# # This will load from the .env.prod file, if and only if
# # the OS env is not setup
# class Settings(BaseSettings):
#     api_key: str = Field(..., alias="api_key")
#     pg_dns: PostgresDsn
#     redis_dns: RedisDsn
#     model_config = SettingsConfigDict(
#         # .env.prod takes a higher priority over the .env
#         env_file=(".env", ".env.prod"), env_file_encoding="utf-8")


# print(Settings().model_dump())


# Setting prefix
class Settings(BaseSettings):
    api_key: str
    pg_dns: PostgresDsn
    redis_dns: RedisDsn
    model_config = SettingsConfigDict(
        # .env.prod takes a higher priority over the .env
        env_file=".env",
        env_file_encoding="utf-8",
        # NOTE: This does not affect the, fields with alias names.
        env_prefix="prod_"
    )


print(Settings().model_dump())

# This will lead to an error if you run the code due to extra fields
# you can add extra="ignore" to avoid this
class Settings(BaseSettings):
    api_key: str = Field(..., alias="api_key")
    pg_dns: PostgresDsn
    redis_dns: RedisDsn
    model_config = SettingsConfigDict(
        # .env.prod takes a higher priority over the .env
        env_file=(".env", ".env.prod"),
        env_file_encoding="utf-8",
        extra="ignore")


print(Settings().model_dump())
