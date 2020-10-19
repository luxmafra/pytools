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
    sender = SenderMock()
    sending_spam = SendingSpam(session, sender)
    sending_spam.send_email(
        'luxmafra@gmail.com',
        'Pytools Course',
        'Testing sending emails...'
    )
    assert len(users) == sender.qtd_email_sent


class SenderMock(Sender):

    def __init__(self):
        super().__init__()
        self.qtd_email_sent = 0
        self.param_sending = None

    def send(self, email_from, email_to, subject, message):
        self.param_sending = (email_from, email_to, subject, message)
        self.qtd_email_sent += 1


def test_param_spam(session):
    user = User(name='Lucas', email='luxmafra@gmail.com')
    session.save(user)
    sender = SenderMock()
    sending_spam = SendingSpam(session, sender)
    sending_spam.send_email(
        'luxchagas@live.com',
        'Pytools Course',
        'Testing sending emails...'
    )
    assert sender.param_sending == (
        'luxchagas@live.com',
        'luxmafra@gmail.com',
        'Pytools Course',
        'Testing sending emails...'
    )
