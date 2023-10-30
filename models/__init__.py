#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv

# Set the storage type based on the environment variable
storage_t = getenv('HBNB_TYPE_STORAGE')

# DBSTORAGE
if storage_t == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
# FILESTORAGE
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage engine
storage.reload()
