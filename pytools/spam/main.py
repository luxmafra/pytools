class SendingSpam:
    def __init__(self, session, sender):
        self.session = session
        self.sender = sender

    def send_email(self, send_from, subject, message):
        for user in self.session.lst():
            self.sender.send(
                send_from,
                user.email,
                subject,
                message
            )
