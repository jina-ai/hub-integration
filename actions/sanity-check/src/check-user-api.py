import requests
import os

_API_HOST = 'https://api.hubble.jina.ai'
_AUTH_TOKEN = os.environ['JINA_AUTH_TOKEN']


def send_request(url: str, token: str=None, data: dict=None, **kwargs):
    headers = {
        'Authorization': f'token {token or _AUTH_TOKEN}'
    }

    return requests.request('POST', url, headers=headers, data=data, **kwargs)

_pat_name = '__created_from_sanity_check__'
_pat_id = None
_pat_token = None

def create_pat():
    global _pat_token

    payload = {
        'name': _pat_name,
        'expirationDays': 1
    }

    url = f'{_API_HOST}/v2/rpc/user.pat.create'
    response = send_request(url, data=payload)
    print('user.pat.create', response.status_code)

    json_res = response.json()
    print(json_res)

    _pat_token = json_res['data']['token']

def list_pat():
    global _pat_id

    url = f'{_API_HOST}/v2/rpc/user.pat.list'
    response = send_request(url, token=_pat_token)
    print('user.pat.list', response.status_code)

    json_res = response.json()
    print(json_res)

    _pat_id = [t for t in json_res['data']['personal_access_tokens'] if t['name']==_pat_name][0]['_id']

def who_am_i():
    url = f'{_API_HOST}/v2/rpc/user.identity.whoami'
    response = send_request(url, token=_pat_token)
    print('user.identity.whoami', response.status_code)

    print(response.json())

def delete_pat():
    url = f'{_API_HOST}/v2/rpc/user.pat.delete'
    response = send_request(url, token=_pat_token, data={'name': _pat_name})
    print('user.pat.delete', response.status_code)

    print(response.json())


create_pat()
who_am_i()
list_pat()
delete_pat()
