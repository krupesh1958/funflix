"""Initializer importing modules"""
from __future__ import annotations

from importlib import import_module


def import_string(dotted_path: str):
    """
    Import a dotted module path and return the attribute/class designated by the last name in the path.
    Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError:
        raise ImportError(
            f"{dotted_path} doen't look like a module path"
        )

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError:
        raise ImportError(
            f'Module "{module_path}" does not define a "{class_name}" attribute/class'
        )
