""""This module contains environment config for the api"""
from os import environ

SECRET_KEY = environ.get("SECRET_KEY")
DATABASE_URL = environ.get("DATABASE_URL")
