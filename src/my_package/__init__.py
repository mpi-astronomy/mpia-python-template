from importlib import metadata

try:
    __version__ = metadata.version(__package__ or __name__)
except:
    __version__ = "dev"