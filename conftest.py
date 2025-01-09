import pytest

pytest_plugins = (
    "pytest_jupyter.jupyter_server",
    "jupyter_server_ydoc.pytest_plugin",
    "jupyter_server_fileid.pytest_plugin"
    "jupyter_server.pytest_plugin",
 )

@pytest.fixture
def jp_server_config(jp_server_config):
    jp_server_config["ServerApp"]["jpserver_extensions"]["jupyter_server_nbmodel"] = True
    return jp_server_config
