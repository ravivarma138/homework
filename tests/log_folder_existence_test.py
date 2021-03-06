"""This makes the test for log file"""
import os

from click.testing import CliRunner

from app  import create_log_folder, create_database

runner=CliRunner()

def log_folder_test():
    response = runner.invoke(create_log_folder)
    assert response.exit_code == 0
    root = os.path.join(root, '../app/logs')
    assert os.path.exists(logdir) is True

def database_check():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    dbdir = os.path.join(root, '../database')
    assert os.path.exists(dbdir) is True