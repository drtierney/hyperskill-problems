class User:
    # create the class attributes
    users = []
    n_active = 0

    # create the __init__ method
    def __init__(self, active, user_name):
        self.user_name = user_name
        self.active = active
        if self.active:
            User.n_active += 1
        User.users.append(self)
