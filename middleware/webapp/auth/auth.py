import requests


class Auth(object):
    def __init__(self):
        self.api_key = "5a8890b0-f02c-440a-a708-41b6fcaff3d8"
        self.client_id = "testing"
        self.client_secret = "d128c12a-d90d-4012-968a-8d14f1ddd57c"

    def login(self):
        url = 'https://api.eka.care/connect-auth/v1/account/login'
        data = {
            "api_key": self.api_key,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        response = requests.post(url, json=data)
        if response.status_code != 200:
            raise Exception("Failed to login")

        resp = response.json()
        access_token = resp.get("access_token")
        if not access_token:
            raise Exception("Failed to login")

        return access_token