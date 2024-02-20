#!/usr/bin/python3
""" Import modules and packages """
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
