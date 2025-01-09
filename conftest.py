import pytest


pytest_plugins = [
    "jupyter_server.pytest_plugin",
    "jupyter_server_fileid.pytest_plugin",
    "jupyter_server_ydoc.pytest_plugin",
]


@pytest.fixture
def jp_server_config(jp_root_dir,jp_server_config):
    print("\n\n\njp_server_config\n",jp_server_config,"\n\n\n")
    print("jp_root_dir\n",jp_root_dir,"\n\n\n")
    return jp_server_config