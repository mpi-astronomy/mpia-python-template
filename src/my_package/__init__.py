from . import _version


try:
    __version__ = _version.version
except Exception:
    __version__ = "dev"
