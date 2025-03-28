from dotenv import load_dotenv
import os

#Load .env file once
load_dotenv()

# This ensures load_dotenv is only called once per interpreter session
_loaded = False

def load_env():
    global _loaded
    if not _loaded:
        load_dotenv(override=False)  # optional: set override=True to force overwrite
        _loaded = True

def get_env_var(key: str, default: str = None) -> str:
    """
    Retrieves an environment variable. 
    Optionally provide a default value if the key is missing.
    """
    value = os.getenv(key)
    if value is None:
        if default is not None:
            return default
        raise ValueError(f"Environment variable '{key}' not found and no default provided.")
    return value


def get_all_env_vars() -> dict:
    """
    Returns a dictionary of all loaded environment variables (only those explicitly listed here).
    """
    return {
        "LOGIN_USERNAME": get_env_var("LOGIN_USERNAME"),
        "LOGIN_PASSWORD": get_env_var("LOGIN_PASSWORD"),
    }
    
    
