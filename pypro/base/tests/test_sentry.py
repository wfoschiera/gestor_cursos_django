from django.test import Client
import pytest


# testa se a página irá gerar um erro. Verificar log no Sentry
@pytest.mark.skip(reason="no way of currently testing this")
def test_sentry_debug(client: Client):
    with pytest.raises(ZeroDivisionError):
        client.get("/sentry-debug/")
