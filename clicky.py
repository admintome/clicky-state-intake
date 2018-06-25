import requests
import json


class Clicky(object):

    def __init__(self, site_id, sitekey):
        self.site_id = site_id
        self.sitekey = sitekey
        self.output = "json"

    def get_data(self, data_type):
        click_api_url = "https://api.clicky.com/api/stats/4"
        payload = {"site_id": self.site_id,
                   "sitekey": self.sitekey,
                   "type": data_type,
                   "output": self.output}
        response = requests.get(click_api_url, params=payload)
        raw_stats = response.text
        return raw_stats

    def get_pages_data(self):
        data = self.get_data("pages")
        return json.loads(data)
