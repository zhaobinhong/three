# coding:utf-8
import json
import os
import random

import three
import unittest
import tempfile
import requests

from flask import jsonify

# from three import Sign
req_id = random.randint(100000, 9999999)
req_id = str(req_id)

SIGNUPDATA = '{"data": {"appkey": "appkey", "uri": "/api/passport/signup/", "req_id": "' + req_id + '","openid": "' + req_id + '"}, "type": "signup"}'
SIGNNINDATA = '{"data": {"appkey": "appkey", "uri": "/api/passport/signin/", "req_id": "' + req_id + '","openid": "' + req_id + '"}, "type": "signin"}'
PAYMENTDATA = '{"data": {"appkey": "appkey", "orderid": "131313123","uri": "/api/passport/payment/", "req_id": "' + req_id + '","openid": "' + req_id + '"}, "type": "payment"}'
RECEIVEDATA = '{"data": {"appkey": "appkey", "orderid": "131313123","uri": "/api/passport/receive/", "req_id": "' + req_id + '","openid": "' + req_id + '"}, "type": "receive"}'
REFUNDSDATA = '{"data": {"appkey": "appkey", "orderid": "131313123","uri": "/api/passport/refunds/", "req_id": "' + req_id + '","openid": "' + req_id + '"}, "type": "refunds"}'

VERIFY = 'http://10.7.7.22:9090'


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, three.app.config['DATABASE'] = tempfile.mkstemp()

        three.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + three.app.config['DATABASE']
        three.app.config['TESTING'] = True

        self.app = three.app.test_client()
        three.init_db()

        print three.app.config['SQLALCHEMY_DATABASE_URI']

        self.init_data()

    def tearDown(self):
        os.close(self.db_fd)
        # os.unlink(three.app.config['DATABASE'])

    def init_data(self):
        pass

    # 注册
    # def test_signup(self):
    #     resp = requests.post(VERIFY + '/Sign', data=SIGNUPDATA)
    #     assert resp.status_code == 200
    #
    #     status = self.app.post('/services/callback/signup', data=resp.content.decode('hex'))
    #     req_status = status.get_data()
    #
    #     print three.Sign.query.all()
    #     user = three.Sign.query.order_by(three.Sign.id).first()
    #     print req_status
    #
    #     assert status.status_code == 200
    # assert user.openid is not None
    # assert status is not None

    # 登录
    # def test_signin(self):
    #     resp = requests.post(VERIFY + '/Sign', data=SIGNNINDATA)
    #     assert resp.status_code == 200
    #     status = self.app.post('/services/callback/signin', data=resp.content.decode('hex'))
    #     req_status = status.get_data()
    #     print req_status
    #     assert status.status_code == 200
    #     js = json.loads(SIGNNINDATA)
    #
    #     valid = self.app.get('/services/login/%s' % js['data']['req_id'])
    #     assert valid.get_data()

    # # 支付
    # def test_payment(self):
    #     self.app.get('/api/passport/payment/')
    #
    #     resp = requests.post(VERIFY + '/Sign', data=PAYMENTDATA)
    #     assert resp.status_code == 200
    #     status = self.app.post('/services/callback/payment', data=resp.content.decode('hex'))
    #     req_status = status.get_data()
    #     print json.loads(req_status).get('detail')
    #     assert status.status_code == 200
    #
    # # 收货
    # # def test_receive(self):
    #     resp = requests.post(VERIFY + '/Sign', data=RECEIVEDATA)
    #     assert resp.status_code == 200
    #     status = self.app.post('/services/callback/receive', data=resp.content.decode('hex'))
    #     req_status = status.get_data()
    #     print json.loads(req_status).get('detail')
    #     assert status.status_code == 200
    #
    # # 退货
    # # def test_refunds(self):
    #     resp = requests.post(VERIFY + '/Sign', data=REFUNDSDATA)
    #     assert resp.status_code == 200
    #     status = self.app.post('/services/callback/refunds', data=resp.content.decode('hex'))
    #     req_status = status.get_data()
    #     print json.loads(req_status).get('detail')
    #     assert status.status_code == 200

    # 存data
    def test_reqdata(self):
        data = '{"data": "lklkl","req_id": "d49a49c0093011e78261480fcf59a86e"}'
        status = self.app.post('/service/requestsreq/', data=data)

        aa = requests.post("http://10.7.7.47:3000/service/requestsreq/", data=data)

        print aa.content
        print aa.status_code
        print status.get_data()
        print status.status_code
        assert status.status_code == 200



if __name__ == '__main__':
    unittest.main()
