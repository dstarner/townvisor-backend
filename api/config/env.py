import os

from dotenv import load_dotenv


__all__ = ['get_env', 'get_path', 'get_bool', 'get_list', 'get_int']

# Load from the .env file if present
load_dotenv()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(  # config
    os.path.dirname(         # api
        os.path.dirname(     # Project root
            os.path.abspath(__file__)
        )
    )
)


def get_env(key, default):
    """Return the environment variable
    """
    return os.getenv(key, default)


def get_path(*args):  # noqa
    """Return the absolute path from the base directory
    """
    return os.path.join(BASE_DIR, *args)


def get_int(name, default=0):
    """Get an integer value from environment variable
    """
    if name not in os.environ:
        return default
    try:
        return int(os.environ[name])
    except:
        return default


def get_bool(name, default=False):  # noqa
    """Get a boolean value from environment variable.

    If the environment variable is not set or value is not one or "true" or
    "false", the default value is returned instead.
    """
    if name not in os.environ:
        return default
    if os.environ[name].lower() in ['true', 'yes', '1']:
        return True
    elif os.environ[name].lower() in ['false', 'no', '0']:
        return False
    else:
        return default


def get_list(name, separator=',', default=None):  # noqa
    """Get a list of string values from environment variable.

    If the environment variable is not set, the default value is returned
    instead.
    """
    if default is None:
        default = []

    if name not in os.environ:
        return default

    value = os.environ[name]
    if separator not in value:
        return value.strip()

    return [x.strip() for x in value.split(separator)]