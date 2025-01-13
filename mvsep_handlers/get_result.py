import requests

def get_result(hash):

    params = {
        'hash': hash,
    }

    response = requests.get('https://mvsep.com/api/separation/get', params=params)
    return response.content