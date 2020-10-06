import pytest

from pytools.spam.email_sender import Sender, InvalidEmail


def test_create_email_sender():
    sender = Sender()
    assert sender is not None


@pytest.mark.parametrize(
    'email_from',
    ['luxmafra@gmail.com', 'lucasmafrachagas@gmail.com']
)
def test_email_from(email_from):
    sender = Sender()
    result = sender.send(
        email_from,
        'luxchagas@live.com',
        'Pytools Course',
        'Testing sending emails...'
    )
    assert email_from in result


@pytest.mark.parametrize(
    'email_from',
    ['', 'luxmafra']
)
def test_email_from_invalid(email_from):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        sender.send(
            email_from,
            'luxchagas@live.com',
            'Pytools Course',
            'Testing sending emails...'
        )
