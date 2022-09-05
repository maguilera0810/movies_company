from django.conf import settings
from requests import get

DELAY_API_URL = settings.DELAY_API_URL


class DelayGateway:

    def __init__(self, delay_time: int = 6000):
        self.delay_time = delay_time

    def call_api_delay(self):
        resp = get(f"{DELAY_API_URL}/{self.delay_time}/",
                   allow_redirects=False)
        print(
            f"Background process excuted correclty after {self.delay_time} ms")
        return True
