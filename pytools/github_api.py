import requests


def buscar_avatar(usuario):
    """
    Search for an user's photo profile from Github

    :param usuario: str
    :return: str with the link of the photo profile
    """
    url = 'https://api.github.com/users/{}'.format(usuario)
    resp = requests.get(url)
    return resp.json()['avatar_url']
