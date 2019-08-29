#!/usr/bin/python3
""" a Python script that takes in 3 strings and sends
a search request to the Twitter API
"""
import sys
import base64
import requests


if __name__ == "__main__":
    client_key = sys.argv[1]
    client_secret = sys.argv[2]
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {'Authorization': 'Basic {}'.format(b64_encoded_key),
                    'Content-Type':
                    'application/x-www-form-urlencoded;charset=UTF-8'}
    auth_data = {'grant_type': 'client_credentials'}
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json().get('access_token')
    search_headers = {'Authorization': 'Bearer {}'.format(access_token)}
    search_params = {'q': sys.argv[3]}
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params)
    l = search_resp.json().get('statuses')[:5]
    for val in l:
        t_id = val.get('id')
        u_text = val.get('text')
        u_name = val.get('user').get('name')
        print("[{}] {} by {}".format(t_id, u_text, u_name))
