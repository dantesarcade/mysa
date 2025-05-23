# API logic to communicate with Mysa cloud

import aiohttp
from pycognito import Cognito

class MysaAPI:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.access_token = None
        self.client = None

    async def login(self):
        self.client = Cognito(
            user_pool_id="us-east-1_example",
            client_id="example_client_id",
            user_pool_region="us-east-1"
        )
        self.client.authenticate(self.email, self.password)
        self.access_token = self.client.access_token

    async def get_devices(self):
        headers = {"Authorization": f"Bearer {self.access_token}"}
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get("https://app-prod.mysa.cloud/v1/devices") as resp:
                return await resp.json()