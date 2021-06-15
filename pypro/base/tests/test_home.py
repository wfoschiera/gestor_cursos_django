from django.test import Client
import pytest


def test_status_code(client: Client):
    resp = client.get('/')
    assert resp.status_code == 200


def test_sentry_debug(client: Client):
    with pytest.raises(ZeroDivisionError):
        client.get('/sentry-debug/')
