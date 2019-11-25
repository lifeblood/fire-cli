import socket
import requests
import json
import ast
import sys
import six
import subprocess


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
    def get_eval_string(name):
        try:
            res = ast.literal_eval(str(name))
        except (ValueError, SyntaxError) as e:
            res = e
        return res

    @staticmethod
    def subprocess_check_call(*command):
        try:
            subprocess.check_call(command, shell=True, executable='/bin/bash')
        except subprocess.CalledProcessError as exc:
            print('run error:', exc.returncode)
            sys.exit(exc.returncode)

    @staticmethod
    def print_fill_char(text):
        # print(text.ljust(80, '*'), flush=True)
        # < left > right ^ center
        six.print_('{:*<80}'.format(text), flush=True)



