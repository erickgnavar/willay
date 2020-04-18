from .base import *  # NOQA

DEBUG = False

INSTALLED_APPS += [  # NOQA
    "raven.contrib.django.raven_compat",
]

RAVEN_CONFIG = {
    "dsn": os.environ.get("DSN_URL"),  # NOQA
}

MINIO_STORAGE_USE_HTTPS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "root": {"level": "WARNING", "handlers": ["sentry"],},  # NOQA
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "sentry": {
            "level": "WARNING",
            "class": "raven.contrib.django.raven_compat.handlers.SentryHandler",
            "tags": {"custom-tag": "x"},
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "raven": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },  # NOQA
        "sentry.errors": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
        "minio_storage": {
            "level": "DEBUG",
            "handlers": ["console", "sentry"],
            "propagate": False,
        },
    },
}
