import pytest


pytest_plugins = [
    "jupyter_server.pytest_plugin",
    "jupyter_server_fileid.pytest_plugin",
    "jupyter_server_ydoc.pytest_plugin",
]


@pytest.fixture
def jp_server_config(jp_root_dir,jp_server_config):
    return {
        "ServerApp": {
            "jpserver_extensions": {
                "jupyter_server_ydoc": True,
                "jupyter_server_nbmodel": True,
                "jupyter_server_fileid": True, 
            },
            "SQLiteYStore": {"db_path": str(jp_root_dir.joinpath(".rtc_test.db"))},
            "BaseFileIdManager": {
                "root_dir": str(jp_root_dir),
                "db_path": str(jp_root_dir.joinpath(".fid_test.db")),
                "db_journal_mode": "OFF",
            },
            "YDocExtension": {"document_save_delay": 1},
            "IdentityProvider": {"token": ""},
            "password":"",
            "disable_check_xsrf": True,
        },
    }
