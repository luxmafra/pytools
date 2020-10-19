from unittest.mock import Mock

import pytest

from pytools.spam.main import SendingSpam
from pytools.spam.models import User


@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Lucas', email='luxmafra@gmail.com'),
            User(name='Renzo', email='luxchagas@live.com')
        ],
        [
            User(name='Lucas', email='luxmafra@gmail.com'),
        ]
    ]
)
def test_sending_spam(session, users):
    for user in users:
        session.save(user)
    sender = Mock()
    sending_spam = SendingSpam(session, sender)
    sending_spam.send_email(
        'luxmafra@gmail.com',
        'Pytools Course',
        'Testing sending emails...'
    )
    assert len(users) == sender.send.call_count


def test_param_spam(session):
    user = User(name='Lucas', email='luxmafra@gmail.com')
    session.save(user)
    sender = Mock()
    sending_spam = SendingSpam(session, sender)
    sending_spam.send_email(
        'luxchagas@live.com',
        'Pytools Course',
        'Testing sending emails...'
    )
    sender.send.assert_called_once_with(
        'luxchagas@live.com',
        'luxmafra@gmail.com',
        'Pytools Course',
        'Testing sending emails...'
    )
