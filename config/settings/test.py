from .base import *  # NOQA

CELERY_TASK_ALWAYS_EAGER = True

# Use regular storage for testing
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
