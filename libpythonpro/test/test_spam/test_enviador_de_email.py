import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['kleber_yokota@hotmail.com', 'foo@bar.com.br'])
def teste_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'kleber_yokota@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Vom Rossum'
    )

    assert destinatario in resultado


@pytest.mark.parametrize('destinatario', ['kleber_yokota', ''])
def teste_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'kleber_yokota@gmail.com',
            'Cursos Python Pro',
            'Primeira turma Guido Vom Rossum'
        )
