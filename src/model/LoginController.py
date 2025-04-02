from src.model.User import User


class LoginController():
    def __init__(self):
        self.users = {"user1":User("user1","abcd")}

    def adduser(self,username,password):
        self.users.update({username,User(username,password)})

    def login(self,username,password):
        print(self.users)
        print(self.users['user1'])
        if username in self.users:
            return self.users[username].checkCredentials(password)
        else:
            return False