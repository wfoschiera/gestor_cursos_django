from model_bakery import baker
import pytest
from django.urls import reverse

from pypro.aperitivos.models import Video
from pypro.base.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return baker.make(Video)


# os testes foram alterados para buscar dinamicamente por videos presentes no DB
@pytest.fixture()
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


# testando caso de insucesso
@pytest.fixture()
def resp_video_nao_encontrado(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug + 'video_nao_existente',)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):
    assert resp_video_nao_encontrado.status_code == 404


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_video_existe(resp, video):
    assert_contains(resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}?')
