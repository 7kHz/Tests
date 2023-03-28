import requests
import unittest
from Settings import YA_TOKEN


class YA:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Authorization': self.token}

    def create_folder(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': path}
        response = requests.put(url, headers=self.get_headers(), params=params)
        print(f'Статус код = {response.status_code}')
        return response.status_code


ya = YA(YA_TOKEN)
path_name = 'YA_2'


class TestCreateFolder(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(ya.create_folder(path_name), 201, 'Папка не была создана!')


if __name__ == '__main__':
    unittest.main()