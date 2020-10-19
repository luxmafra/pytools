class Sender:
    def __init__(self):
        self.qtd_email_sent = 0

    def send(self, email_from, email_to, subject, message):
        if '@' not in email_from:
            raise InvalidEmail('Email address of the sender is invalid: {}'.format(email_from))
        self.qtd_email_sent += 1
        return email_from


class InvalidEmail(Exception):
    pass
