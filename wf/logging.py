CONFIG = {
    'version': 1,
    "disable_existing_loggers": False,
    'formatters': {
        'default': {
            "()": "logging.Formatter",
            "fmt": "%(name)s - %(levelname)s - %(message)s",
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            "stream": "ext://sys.stderr",
        },
    },
    'loggers': {
        'root': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        "watchdog": {
            "handlers": ["default"],
            "level": "ERROR",
            "propagate": True,
        },
        "PIL": {
            "handlers": ["default"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}
