"""Email Clients."""

"""The Python Email Automation Framework."""
try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore


__all__ = ["email_manager", "gmail"]
