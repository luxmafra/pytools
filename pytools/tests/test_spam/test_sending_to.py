import pytest

from pytools.spam.email_sender import Sender
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
    sender = Sender()
    sending_spam = SendingSpam(session, sender)
    sending_spam.send_email(
        'luxmafra@gmail.com',
        'Pytools Course',
        'Testing sending emails...'
    )
    assert len(users) == sender.qtd_email_sent
