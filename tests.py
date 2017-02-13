# coding:utf-8
import os
import three
import unittest
import tempfile
import requests

from flask import jsonify

SIGNUPDATA = '{"data": {"appkey": "appkey", "uri": "/api/passport/signup/", "req_id": "c51ce410c124a10e0db5e4b97fc2af39"}, "type": "signup"}'
VERIFY = 'http://10.7.7.22:9090'


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, three.app.config['DATABASE'] = tempfile.mkstemp()
        three.app.config['TESTING'] = True
        self.app = three.app.test_client()
        # three.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(three.app.config['DATABASE'])

    # 登录
    def test_signup(self):
        resp = requests.post(VERIFY + '/Sign', data=SIGNUPDATA)
        # print resp.content
        assert resp.status_code == 200
        status = self.app.post('/services/callback/signup', data=resp.content.decode('hex'))
        req_status = status.get_data()
        print req_status
        # print jsonify(req_status)

        assert status.status_code == 200
        # assert status is not None


if __name__ == '__main__':
    unittest.main()
