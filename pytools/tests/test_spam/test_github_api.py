from unittest.mock import Mock

from pytools import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'luxmafra', 'id': 69525183,
        'avatar_url': 'https://avatars2.githubusercontent.com/u/69525183?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('luxmafra')
    assert 'https://avatars2.githubusercontent.com/u/69525183?v=4' == url
