"""Settings module."""
import os
import sys

import redis
from loguru import logger


class PQCConfig:
    """PQCConfig class."""

    __VERSION__ = "0.1.0"
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "10")


logger.remove()
logger.add(sys.stdout, format="{time} | {level} | {message} | {extra}", colorize=True)
redis_cache = redis.Redis(host=PQCConfig.REDIS_HOST, port=PQCConfig.REDIS_PORT, db=8, password=PQCConfig.REDIS_PASSWORD)
