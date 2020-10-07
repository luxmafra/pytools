import pytest

from pytools.spam.db import Connect
from pytools.spam.models import User


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


def test_save_user(session):
    user = User(name='Lucas')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Lucas'), User(name='Renzo')]
    for user in users:
        session.save(user)
    assert users == session.lst()
