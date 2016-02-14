import os
_BASE_DIR = os.path.dirname(__file__)

DATABASES_ENGINE = 'django.db.backends.sqlite3'
DATABASES_NAME = os.path.join(_BASE_DIR, 'db.sqlite3')
DATABASES_USER = None
DATABASES_PASSWORD = None
DATABASES_HOST = None
DATABASES_PORT = None

ORIGIN = 'http://localhost:8000'
DEFAULT_XPUB = 'xpub6BmJBbHkjXnr82jg4JdNsGAzsZeyCzeXfPJo7UtmsMfiJ5hqB3xGnocSvfbAXGKoC8GCiTGM7mVR9QNWtECScVS1ANswyE7CvMFmk5UiQ8o'
