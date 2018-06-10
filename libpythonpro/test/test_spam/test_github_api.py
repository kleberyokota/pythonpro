from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars2.githubusercontent.com/u/109299?v=4'
    resp_mock.json.return_value = {
        'login': 'kleberyokota', 'id': 39857180,
        'avatar_url': url
    }
    get_original = github_api.request.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.request.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('kleber')
    assert avatar_url == url


def test_buscar_avatar():
    url = github_api.buscar_avatar('kleber')
    assert 'https://avatars2.githubusercontent.com/u/109299?v=4' == url
