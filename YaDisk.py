import requests


class YaDisk:
    def __init__(self, access_token_ya):
        self.access_token_ya = access_token_ya

    def connection_status(self):
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.access_token_ya}'}
        url = 'https://cloud-api.yandex.net/v1/disk'
        res = requests.get(url=url, headers=headers)
        return res.status_code

    def create_folder(self, folder):
        """ Метод создает папку на яндекс диске"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.access_token_ya}'}
        params = {'path': folder, 'overwrite': 'true'}
        requests.put(url, headers=headers, params=params)


