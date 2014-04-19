#Imports
import sys
from vyos_session import utils

print sys.path

def test_filehandle():
    """
    Check if log file exists. Create it if not.
    """
    assert utils.get_log_filehandler() is not False

def test_init_logger():
    """
    Assert that multiple calls of init_logger() return the same logger object.
    """
    logger1 = utils.init_logger()
    logger2 = utils.init_logger()
    assert logger1 == logger2

def test_loglevel():
    """
    Test log level severity
    """
    assert utils.get_log_level() in ['DEBUG','INFO','WARN','ERROR','CRITICAL']