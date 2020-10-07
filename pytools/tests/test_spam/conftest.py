import pytest

from pytools.spam.db import Connect


@pytest.fixture(scope='session')
def connect():
    # Setup
    connect_obj = Connect()
    yield connect_obj
    # Tear Down
    connect_obj.close()


@pytest.fixture
def session(connect):
    session_obj = connect.generate_session()
    yield session_obj
    session_obj.roll_back()
    session_obj.close()