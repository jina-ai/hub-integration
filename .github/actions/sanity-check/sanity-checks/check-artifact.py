import json
import requests
import os

_API_HOST = 'https://api.hubble.jina.ai'
_AUTH_TOKEN = os.environ['JINA_AUTH_TOKEN']


def send_request(url: str, data: dict, **kwargs):
    headers = {
        'Authorization': f'token {_AUTH_TOKEN}'
    }

    return requests.request('POST', url, headers=headers, data=data, **kwargs)

def upload(id: str = None):
    payload = {
        'metaData': json.dumps({'foo': 'bar'}),
        'public': False,
    }

    if id:
        payload['id'] = id

    files=[
        ('file',('manifest.yml',open('./sanity-checks/executors/SanityCheck/manifest.yml','rb'),'application/octet-stream'))
    ]

    url = f'{_API_HOST}/v2/rpc/artifact.upload'
    response = send_request(url, data=payload, files=files)
    print('artifact.upload', response.status_code)

    return response.json()

def update_metadata(id: str):
    payload = {
        'id': id,
        'metaData': json.dumps({'foo': 'bar'}),
    }

    url = f'{_API_HOST}/v2/rpc/artifact.updateMetaData'
    response = send_request(url, data=payload)
    print('artifact.updateMetaData', response.status_code)

def get_download_url(id: str):
    url = f'{_API_HOST}/v2/rpc/artifact.getDownloadUrl'
    response = send_request(url, data={'id': id})

    print('artifact.getDownloadUrl', response.status_code)

def get_detail(id: str):
    url = f'{_API_HOST}/v2/rpc/artifact.getDetail'
    response = send_request(url, data={'id': id})

    print('artifact.getDetail', response.status_code)

def delete(id: str):
    url = f'{_API_HOST}/v2/rpc/artifact.delete'
    response = send_request(url, data={'id': id})

    print('artifact.delete', response.status_code)


def run():
    id = upload()['data']['_id']
    upload(id)
    update_metadata(id)
    get_download_url(id)
    get_detail(id)
    delete(id)

run()
