from libpythonpro.spam.models import Usuario


def test_salva_usuario(sessao):
    usuario = Usuario(nome='Kleber', email='kleber_yokota@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome ='Kleber', email='kleber_yokota@hotmail.com'),
                Usuario(nome='Renzo', email='kleber_yokota@hotmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
