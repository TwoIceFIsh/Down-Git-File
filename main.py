import json
import os

import requests


class Loadinfo:

    def __init__(self, file_path: str):
        self._OWNER = "TwoIceFIsh"
        self._REPO = "Spring-Boot-K0konutz"
        self._response = requests.get(f'https://api.github.com/repos/{self._OWNER}/{self._REPO}/releases/latest')
        self._json_ob = json.loads(self._response.text)
        self.ASSET_ID = self._json_ob['assets'][0]['id']
        self.DOWN_URL = self._json_ob['assets'][0]['browser_download_url']
        self.FILE_NAME = self._json_ob['assets'][0]['name']
        self.PATH = file_path
        self.FULL_PATH = os.path.join(self.PATH, self.FILE_NAME)

    def down_file(self):
        self.__response = requests.get(self.DOWN_URL)
        with open(os.path.join(self.PATH, self.FILE_NAME), 'wb') as f:
            f.write(self.__response.content)


info = Loadinfo(file_path='')
info.down_file()

os.system(info.FULL_PATH)
