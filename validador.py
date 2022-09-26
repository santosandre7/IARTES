import re
class Validador(object):
    def __init__(self):
        self._cod_area = (11, 12, 19, 65, 68, 92, 93)

    def ano_bissexto(self, ano):
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            return True
        else:
            return False

    def validar_data(self, data):
        dia = int(data[:2])
        mes = int(data[3:5])
        ano = int(data[6:])
        meses_de_31 = (1, 3, 5, 7, 8, 10, 12)
        meses_de_30 = (4, 6, 9, 11)

        ano_valido = False
        if ano > 0 and len(data[6:])==4:
            ano_valido = True

        mes_valido = False
        if mes > 0 and mes < 13:
           mes_valido = True

        dia_valido = False
        if dia > 0 and dia < 32:
            if dia == 31:
                if mes in meses_de_31:
                    dia_valido = True
            elif dia == 30:
                if mes in meses_de_30 or mes in meses_de_31:
                    dia_valido = True
            elif dia == 29:
                if mes != 2:
                    dia_valido = True
                elif mes == 2 and self.ano_bissexto(ano):
                    dia_valido = True
            else:
                dia_valido = True

        data_valida = False
        if ano_valido and mes_valido and dia_valido:
            data_valida = True

        return data_valida

    # (92)999679090
    def validar_telefone(self, telefone):

        telefone_valido = True
        if len(telefone) != 13:
            telefone_valido = False
        elif len(telefone[4:]) != 9:
            telefone_valido = False
        elif telefone[0] != '(' or telefone[3] != ')':
            telefone_valido = False
        elif int(telefone[1:3]) not in self._cod_area:
            telefone_valido = False

        return telefone_valido



    def validar_cpf(self, cpf):

        cpf_valido = True
        if len(cpf) != 14:
            cpf_valido = False
        elif cpf[3] != ".":
            cpf_valido = False
        elif cpf[7] != ".":
            cpf_valido = False
        elif cpf[-3] != "-":
            cpf_valido = False
        elif cpf_valido:
            while True:
                novo_cpf = cpf[:-2]
                reverso = 10
                total = 0

                for index in range(19):
                    if index > 8:
                        index -= 9
                    total += int(novo_cpf[index])
                    if reverso < 2:
                        reverso = 11
                        d = 11 - (total % 11)
                        if d > 9:
                            d = 0
                            total = 0
                            novo_cpf += str(d)

                sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

                if cpf == novo_cpf and not sequencia:
                    cpf_valido = True
                else:
                    cpf_valido = False

        return cpf_valido


    def validar_email(self, email):

        email_valido = True
        pattern = '/^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i'

        if re.search(pattern, email):
            email_valido = True
        else:
            email_valido = False

        return email_valido
