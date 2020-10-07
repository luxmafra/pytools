from pytools.spam.db import Connect
from pytools.spam.models import User


def test_save_user():
    connect = Connect()
    session = connect.generate_session()
    user = User(name='Lucas')
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()
    session.close()
    connect.close()


def test_list_users():
    connect = Connect()
    session = connect.generate_session()
    users = [User(name='Lucas'), User(name='Renzo')]
    for user in users:
        session.save(user)
    assert users == session.lst()
    session.roll_back()
    session.close()
    connect.close()
