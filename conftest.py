import pytest

pytest_plugins = (
    "pytest_jupyter.jupyter_server",
    "jupyter_server_ydoc.pytest_plugin",
    "jupyter_server_fileid.pytest_plugin",
    "jupyter_server.pytest_plugin"
 )