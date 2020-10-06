class Sender:
    def send(self, email_from, email_to, subject, message):
        if '@' not in email_from:
            raise InvalidEmail('Email address of the sender is invalid: {}'.format(email_from))
        return email_from


class InvalidEmail(Exception):
    pass
