from pytools.spam.models import User


def test_save_user(session):
    user = User(name='Lucas')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_users(session):
    users = [User(name='Lucas'), User(name='Renzo')]
    for user in users:
        session.save(user)
    assert users == session.lst()
