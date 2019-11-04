import socket
import requests
import json
import ast


class Utils(object):
    _GET = 'GET'
    _POST = 'POST'

    def __init__(self):
        pass

    @classmethod
    def get_ip(cls):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        return ip

    @staticmethod
    def _request(method, **kwargs):
        try:
            json_parse_exception = json.decoder.JSONDecodeError
        except AttributeError:  # Python 2
            json_parse_exception = ValueError

        try:
            res = requests.request(method, **kwargs)
        except requests.RequestException as e:
            print(e)
        else:
            try:
                return res.json()
            except json_parse_exception as e:
                print(e)

    @classmethod
    def get_http_json(cls, **kwargs):
        return json.loads(json.dumps(cls._request(cls._GET, **kwargs)))

    @classmethod
    def post_http_json(cls, **kwargs):
        return json.loads(json.dumps(cls._request(cls._POST, **kwargs)))

    @staticmethod
    def eval(name):
        try:
            res = ast.literal_eval(name)
        except (ValueError, SyntaxError) as e:
            res = e
        return res



