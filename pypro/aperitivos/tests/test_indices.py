import pytest
from django.urls import reverse


from pypro.base.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    ['Video Aperitivo: Motivação',
     'Instalação Windows',
     ])
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


@pytest.mark.parametrize(
    'slug',
    ['motivacao',
     'instalacao-windows',
     ])
def test_slug_video(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp,
                    f'href="{video_link}"')  # vou explicitar que quero que contenha o link (a href) dentro do template
