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
        pass

    def close(self):
        pass


class Connect:
    def generate_session(self):
        return Session()

    def close(self):
        pass