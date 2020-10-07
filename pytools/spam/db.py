from time import sleep


class Session:
    cont = 0
    users = []

    def save(self, user):
        Session.cont += 1
        user.id = Session.cont
        self.users.append(user)

    def lst(self):
        return self.users

    def roll_back(self):
        self.users.clear()

    def close(self):
        pass


class Connect:

    def __init__(self):
        sleep(10)

    def generate_session(self):
        return Session()

    def close(self):
        pass
