"""Settings module - automatically loads correct settings based on ENV variable.

Usage:
    from src.settings import settings
    print(settings.app_name)

    You can add more environments using the same pattern.

Explanation:
    Pydantic loads .env file after instantiating the Settings class.
    By checking env attribute on base Settings instance, we don't have to worry about
    loading the .env file manually.
"""

import datetime
import logging
import logging.config
import os
from pydantic import model_validator
from pydantic_settings import BaseSettings

# program run timestamp, meant to be static per program run (to separate logs and outputs per run)
TIMESTAMP: str = datetime.datetime.now().strftime("%Y%m%d_%H-%M-%S-%f")


class Settings(BaseSettings):
    """Local configuration, used as a base for other environments."""

    settings_type: str = "base"
    project_root: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    env: str = os.getenv("env", "local")
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

    logs_dir: str = os.path.join(project_root, "local", "logs")
    current_run_logs_dir: str = os.path.join(logs_dir, "runs", f"{TIMESTAMP}")
    log_level: str | int = logging.INFO
    logging_config: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
            "console": {
                "format": "%(asctime)s [%(levelname)s] %(message)s",
                "datefmt": "%H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "level": log_level,
                "formatter": "console",
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
            },
            "debug_file": {
                "level": logging.DEBUG,
                "formatter": "standard",
                "class": "logging.FileHandler",
                "filename": os.path.join(
                    current_run_logs_dir,
                    f"debug.log",
                ),
            },
            "info_file": {
                "level": logging.INFO,
                "formatter": "console",
                "class": "logging.FileHandler",
                "filename": os.path.join(
                    current_run_logs_dir,
                    f"info.log",
                ),
            },
            "current_info": {
                "level": logging.INFO,
                "formatter": "console",
                "class": "logging.FileHandler",
                "filename": os.path.join(logs_dir, "current_info.log"),
                "mode": "w",
            },
            "current_debug": {
                "level": logging.INFO,
                "formatter": "standard",
                "class": "logging.FileHandler",
                "filename": os.path.join(logs_dir, "current_debug.log"),
                "mode": "w",
            },
            # "debug_rotating": {  # for long running programs use this instead of debug_file
            #     "level": logging.DEBUG,
            #     "formatter": "standard",
            #     "class": "logging.handlers.TimedRotatingFileHandler",
            #     "filename": os.path.join(logs_dir, "debug.log"),
            #     "when": "midnight",
            #     "backupCount": 7,  # keep 7 days
            #     "utc": True,
            # },
            # "info_rotating": {  # for long running programs use this instead of info_file
            #     "level": logging.INFO,
            #     "formatter": "console",
            #     "class": "logging.handlers.TimedRotatingFileHandler",
            #     "filename": os.path.join(logs_dir, "info.log"),
            #     "when": "midnight",
            #     "backupCount": 7,  # keep 7 days
            #     "utc": True,
            # },
        },
        "loggers": {
            "": {  # root logger
                "handlers": [
                    "console",
                    "debug_file",
                    "info_file",
                    "current_info",
                    "current_debug",
                ],
                "level": logging.DEBUG,
                "propagate": False,
            },
        },
    }

    def configure_logging(self):
        """Configure logging based on settings.

        This method should be ran once at the start of the application.
        """
        os.makedirs(self.current_run_logs_dir, exist_ok=True)
        logging.config.dictConfig(self.logging_config)

        logger = logging.getLogger(__name__)
        logger.info(f"Logging configured. Logs directory: {self.logs_dir}")


class TestSettings(Settings):
    """Settings for test environment with test-specific overrides."""

    settings_type: str = "test"


#### Add your test configuration above this line. Add 'if' condition for it below. ####

settings = Settings()

if settings.env == "test":
    settings = TestSettings()

# Export for convenience
__all__ = ["settings"]
