import pytest


pytest_plugins = [
    "pytest_jupyter.jupyter_server",
    "jupyter_server.pytest_plugin",
    "jupyter_server_fileid.pytest_plugin",
    "jupyter_server_ydoc.pytest_plugin"
]

#jp_server_config
#  {'ServerApp': {'jpserver_extensions': {'jupyter_server_ydoc': True, 'jupyter_server_fileid': True}, 'token': '', 'password': '', 'disable_check_xsrf': True}, 'SQLiteYStore': {'db_path': '/tmp/pytest-of-runner/pytest-0/test_post_input_execute0/root_dir/.rtc_test.db'}, 'BaseFileIdManager': {'root_dir': '/tmp/pytest-of-runner/pytest-0/test_post_input_execute0/root_dir', 'db_path': '/tmp/pytest-of-runner/pytest-0/test_post_input_execute0/root_dir/.fid_test.db', 'db_journal_mode': 'OFF'}, 'YDocExtension': {'document_save_delay': 1}} 

#ArbitraryFileIdManager

# jp_root_dir
#  /tmp/pytest-of-runner/pytest-0/test_post_input_execute0/root_dir

#Changing Nothing passes
#try to pass config as above using jp_root_dir too, if 404 persists try adding server in plugins


#FIXME if not, here's a msg to Mike
# I suspect the CI failures are related to the inability to connect to the database. However, the database connection works correctly in the local environment.
# Here's the CI error:
# ![image](https://github.com/user-attachments/assets/21e55616-7741-4a6e-a0b9-b9a75aa50a41)

# similar tests pass in Jupyter Collaborator, where the database connection is successfully established
# ![image](https://github.com/user-attachments/assets/6754b520-cd9f-47ff-9cf7-67bad3ad6b80)

@pytest.fixture
def jp_server_config(jp_root_dir,jp_server_config):
    return {
        'ServerApp': {
            'jpserver_extensions': {
                'jupyter_server_ydoc': True,
                'jupyter_server_fileid': True,
                'jupyter_server_nbmodel': True,
                'jupyter_events': True
            },
            'token': '',
            'password': '',
            'disable_check_xsrf': True},
             "SQLiteYStore": {"db_path": str(jp_root_dir.joinpath(".rtc_test.db"))},
            "BaseFileIdManager": {
                "root_dir": str(jp_root_dir),
                "db_path": str(jp_root_dir.joinpath(".fid_test.db")),
                "db_journal_mode": "OFF",
            },
            'YDocExtension': {
                'document_save_delay': 1
            }
    } 
