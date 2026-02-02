"""Settings module - automatically loads correct settings based on ENV variable.

Usage:
    from src.settings import settings
    print(settings.app_name)

    You can add more envionrments using the same pattern.

Explanation:
    Pydantic loads .env file after instantiating the Settings class.
    By checking env attribute on base Settings instance, we don't have to worry about
    loading the .env file manually.
"""

import os
from pydantic_settings import BaseSettings


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


class TestSettings(Settings):
    """Settings for test environment with test-specific overrides."""

    settings_type: str = "test"


#### Add your test configuration above this line. Add 'if' condition for it below. ####

settings = Settings()

if settings.env == "test":
    settings = TestSettings()

# Export for convenience
__all__ = ["settings"]
