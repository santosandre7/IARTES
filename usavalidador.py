import validador as val

def main():
    v = val.Validador()
    base_dados = []
    for i in range(0,1000):
        telefone = input("Informe Telefone: ")
        data = input("Informe data: ")
        cpf = input("Informe CPF: ")
        email = input("Informe o email: ")

        if not v.validar_telefone(telefone):
            print("Telefone Inválido")
        elif not v.validar_data(data):
            print("Data inválida")
        elif not v.validar_cpf(cpf):
            print("CPF Inválido")
        elif not v.validar_email(email):
            print("Email Inválido")
        else:
            entrada = {"telefone":telefone, "data": data, "cpf": cpf, "email": email}
            base_dados.append(entrada)


if __name__ == "__main__":
    main()