class Enviador:
    def enviar(self, remente, destinatario, assunto, corpo):
        if '@' not in remente:
            raise EmailInvalido(f'Email do remente invalido: {remente}')
        return remente


class EmailInvalido(Exception):
    pass
