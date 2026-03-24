import urllib.request
import urllib.parse
import json


class BaseClient:
    def __init__(self, base_url, timeout=10, headers=None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.headers = headers or {}

    def build_url(self, endpoint="", params=None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        if params:
            query = urllib.parse.urlencode(params)
            url = f"{url}?{query}"
        return url

    def fetch(self, endpoint="", params=None):
        url = self.build_url(endpoint, params)

        req = urllib.request.Request(url, headers=self.headers)
        with urllib.request.urlopen(req, timeout=self.timeout) as res:
            raw = res.read().decode("utf-8")

        return self.parse_json(raw)

    def parse_json(self, raw_data):
        try:
            return json.loads(raw_data)
        except json.JSONDecodeError:
            return {
                "error": "Invalid JSON",
                "raw": raw_data
            }

    
    def jsonify(self, data, pretty=True):

        if pretty:
            return json.dumps(data, indent=2, sort_keys=True)
        return json.dumps(data)
