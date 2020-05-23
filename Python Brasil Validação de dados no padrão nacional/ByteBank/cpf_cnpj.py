from validate_docbr import CPF, CNPJ

class Documento:
    def cria_documento(self, documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return  DocCnpj(documento)
        else:
            raise ValueError("Documento inválido!")

class DocCnpj:
    def __init__(self, documento):
        valida = CNPJ()
        if valida.validate(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!")

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()

class DocCpf:
    def __init__(self, documento):
        valida = CPF()
        if valida.validate(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!")

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format()
