from pytools.spam.email_sender import Sender
from pytools.spam.main import SendingSpam


def test_sending_spam(session):
    sending_spam = SendingSpam(session, Sender())
    sending_spam.send_email(
        'luxmafra@gmail.com',
        'Pytools Course',
        'Testing sending emails...'
    )
