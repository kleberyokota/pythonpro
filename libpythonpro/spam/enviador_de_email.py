class Enviador:
    def __init__(self):
        self.qtd_email_enviados = 0

    def enviar(self, remente, destinatario, assunto, corpo):
        if '@' not in remente:
            raise EmailInvalido(f'Email do remente invalido: {remente}')
        self.qtd_email_enviados += 1
        return remente


class EmailInvalido(Exception):
    pass
