import unittest
from unittest.case import TestCase
import YaDisk
from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")


class TestYaDisk(TestCase):

    def test_link_to_yadisk(self):
        access_token_ya = os.getenv("access_token_ya")
        ya = YaDisk.YaDisk(access_token_ya)
        res = ya.connection_status()
        self.assertEqual(res, 200)

    def test_link_to_yadisk_negative(self):
        access_token_ya = ''
        ya = YaDisk.YaDisk(access_token_ya)
        res = ya.connection_status()
        self.assertNotEqual(res, 200)

    def test_get_folder(self):
        access_token_ya = os.getenv("access_token_ya")
        folder = "new_folder"
        path = f"disk:/{folder}"
        ya = YaDisk.YaDisk(access_token_ya)
        ya.create_folder(folder)
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {access_token_ya}'}
        params = {'path': path}
        result = requests.get(url, headers=headers, params=params)
        self.assertEqual(result.json().get('path'), path)


if __name__ == '__main__':
    unittest.main()
