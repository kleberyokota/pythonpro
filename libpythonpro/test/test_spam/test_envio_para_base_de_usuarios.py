import pytest

from libpythonpro.spam.enviador_de_email import Enviador
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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'kleber_yokota@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantasticos'
    )

    assert len(usuarios) == enviador.qtd_email_enviados