class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def getPassword(self):
        return self.password
    
    def getUsername(self):
        return self.username
    
    def checkCredentials(self, password):
        return password == self.password