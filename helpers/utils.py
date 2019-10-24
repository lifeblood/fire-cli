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
            res = requests.request(method, **kwargs)
        except requests.RequestException as e:
            print(e)
        else:
            try:
                return res.json()
            except json.decoder.JSONDecodeError as e:
                print(e)

    @classmethod
    def http_get_json(cls, **kwargs):
        cls._request(cls._GET, **kwargs)

    @classmethod
    def http_post_json(cls, **kwargs):
        cls._request(cls._POST, **kwargs)

    @staticmethod
    def eval(name):
        try:
            res = ast.literal_eval(name)
        except (ValueError, SyntaxError) as e:
            res = e
        return res



