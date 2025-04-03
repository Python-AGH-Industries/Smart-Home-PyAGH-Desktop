from src.model.user import User

class LoginController():
    def __init__(self):
        self.users = {"a": User("a","a")}

    def adduser(self,username,password):
        self.users.update({username, User(username, password)})

    def login(self,username,password):
        print(self.users)
        print(self.users['a'])
        if username in self.users:
            return self.users[username].checkCredentials(password)
        else:
            return False