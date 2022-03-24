
class Contact:
    def __init__(self, name="", email="", month="",day=""):
        self.name = name
        self.email = email
        self.month = month
        self.day = day

    def return_self_list_append_one(self):
        return [self.name, self.email, self.month, self.day, 1]

    def return_self_list_append(self, increased=1):
        return [self.name, self.email, self.month, self.day, increased]