from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.models import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [

            Usuario(nome='Kleber', email='kleber_yokota@hotmail.com'),
            Usuario(nome='Renzo', email='renzo@python.pro.br')
        ],
        [

            Usuario(nome='Kleber', email='kleber_yokota@hotmail.com')

        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kleber_yokota@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )

    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='kleber', email='kleber_yokota@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'lucioano@python.pro.br',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'lucioano@python.pro.br',
        'kleber_yokota@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )
