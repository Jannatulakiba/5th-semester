# get_config.py
"""
Global configuration for Bangladesh_Crop_Recommendation package.
This file is imported by data/validation.py using:
from .. import get_config as _get_config
"""

# Example configuration dictionary
CONFIG = {
    "version": "1.0.0",
    "allow_nan": False,
    "debug": True,
}

def get_config(key=None):
    """
    Retrieve global configuration.
    If key is None → return full config.
    If key exists → return that specific value.
    """
    if key is None:
        return CONFIG
    return CONFIG.get(key, None)

# Simple test function (optional)
def some_function():
    return "get_config loaded successfully!"
