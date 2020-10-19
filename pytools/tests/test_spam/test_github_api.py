from unittest.mock import Mock

import pytest

from pytools import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/69525183?v=4'
    resp_mock.json.return_value = {
        'login': 'luxmafra', 'id': 69525183,
        'avatar_url': url
    }
    get_mock = mocker.patch('pytools.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('luxmafra')
    assert avatar_url == url


def test_buscar_avatar_integration():
    url = github_api.buscar_avatar('luxmafra')
    assert 'https://avatars2.githubusercontent.com/u/69525183?v=4' == url
