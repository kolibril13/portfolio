# twitter class

import requests

class Tweet():
    def __init__(self, s):
        api = f'https://publish.twitter.com/oembed?url={s}'
        response = requests.get(api)
        self.text = response.json()["html"]

    def _repr_html_(self):
        return self.text