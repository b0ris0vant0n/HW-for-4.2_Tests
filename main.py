import requests
import json

folder_name = 'Папка для ДЗ'
url = 'https://cloud-api.yandex.net/v1/disk/resources'
token = ''
headers = {
             'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
            }

def create_folder(folder_name):
    params = {'path': folder_name, "overwrite": "false"}
    response = requests.put(url, headers=headers, params=params)
    response.raise_for_status
    return response.status_code

def get_folder_type(folder_name):
    params = {'path': folder_name}
    result = requests.get(url, headers=headers, params=params)
    if result.status_code == 200:
        result_dict = json.loads(result.text)
        return result_dict.get('type')

if __name__ == '__main__':
    create_folder(folder_name)



