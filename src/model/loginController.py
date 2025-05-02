import requests
import json

class LoginController():

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(LoginController, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.initialized = False

        return cls._instance

    def __init__(self):
        if not self.initialized:
            self.session = requests.session()
            self.initialized = True

    def login(self, username, password):
        res = json.loads(self.session.post(
            'http://127.0.0.1:5000/login',
            json = {
                "username": username,
                "password": password
                }
            ).text
        )

        if res['success']:
            return True
        else:
            return False
        
    def getSensors(self,type_id):
        res = self.session.post('http://127.0.0.1:5000/getUserSensors', json={"type_id":type_id})
        return json.loads(res.text)
    
    def getSensorData(self,sensor_id):
        res = self.session.post('http://127.0.0.1:5000/readSensorData', json={"sensor_id":sensor_id})
        return json.loads(res.text)
