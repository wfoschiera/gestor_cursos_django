import pytest
from django.urls import reverse

from pypro.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp):
    assert_contains(resp, '<h1 class="mt-2 mb-3">Video Aperitivo: Motivação</h1>')


def test_video_existe(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/569032237?')
