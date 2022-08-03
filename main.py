import argparse
import json
import os
import time
from datetime import datetime

import psutil as psutil
import requests


class Loadinfo:

    def __init__(self, owner: str, repo: str):
        self._OWNER = owner
        self._REPO = repo
        self._response = requests.get(f'https://api.github.com/repos/{self._OWNER}/{self._REPO}/releases/latest')
        self.repo_url = f'https://api.github.com/repos/{self._OWNER}/{self._REPO}/releases/latest'
        self._json_ob = json.loads(self._response.text)
        self.ASSET_ID = self._json_ob['assets'][0]['id']
        self.DOWN_URL = self._json_ob['assets'][0]['browser_download_url']
        self.FILE_NAME = self._json_ob['assets'][0]['name']
        self.PATH = os.path.curdir
        self.FULL_PATH = os.path.join(self.PATH, self.FILE_NAME)

    def down_file(self):
        self.__response = requests.get(self.DOWN_URL)
        with open(os.path.join(self.PATH, self.FILE_NAME), 'wb') as f:
            f.write(self.__response.content)

    def save_info(self):
        return True


parser = argparse.ArgumentParser(description='python Implementation')
parser.add_argument('-o', help='seqDistVarCont <*> weights', required=True)
parser.add_argument('-r', help='seqDistVarCont <*> weights', required=True)

args = parser.parse_args()
info = Loadinfo(owner=args.o, repo=args.r)

while True:
    print(f"[!] {datetime.now().strftime('%Y-%m-%d %H:%M')} : Update check...({info.repo_url})")
    time.sleep(600)


def ss():
    info = Loadinfo(file_path='')
    info.down_file()

    # version check

    # process kill and start
    for proc in psutil.process_iter():
        process_name = proc.name()
        print(process_name)
        process_pid = proc.pid

        if process_name == '':
            process = psutil.Process(process_pid)
            process.kill()
            os.system(info.FULL_PATH)
