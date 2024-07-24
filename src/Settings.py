import os
from dotenv import dotenv_values


def get_config():
    config = dotenv_values()
    return config
