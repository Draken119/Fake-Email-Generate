import random
import string

class AccountTemp:
    def __init__(self):
        self.email = self.generate_email()
        self.password = self.generate_password()

    def generate_email(self):
        email_length = 10
        email_domain = "@example.com"
        random_string = ''.join(random.choices(string.ascii_lowercase, k=email_length))
        email = random_string + email_domain
        return email

    def generate_password(self):
        password_length = 8
        password_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choices(password_chars, k=password_length))
        return password

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password


emails = []

while True:
    print("Selecione uma opção:")
    print("1. Gerar novo email")
    print("10. Apagar emails")
    print("11. Receber mensagens")
    print("0. Sair")

    option = input("Opção: ")

    if option == "1":
        account = AccountTemp()
        emails.append(account)
        print("Novo email gerado:")
        print("Email: " + account.get_email())
        print("Senha: " + account.get_password())
        print()

    elif option == "10":
        emails = []
        print("Emails apagados com sucesso!")
        print()

    elif option == "11":
        if len(emails) == 0:
            print("Não há emails disponíveis. Gere um novo email primeiro.")
        else:
            print("Selecione um email:")
            for i, email in enumerate(emails):
                print(f"{i + 1}. {email.get_email()}")

            email_index = input("Opção: ")

            try:
                email_index = int(email_index)
                if 1 <= email_index <= len(emails):
                    email = emails[email_index - 1]
                    print("Mensagem recebida:")
                    print("Gmail: " + email.get_email())
                    print("Subject: verify code")
                    verification_code = ''.join(random.choices(string.digits, k=6))
                    print("Message: You telegram code verification is " + verification_code + ". Do not share with anyone!")
                    print()
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Opção inválida. Tente novamente.")

    elif option == "0":
        break

    else:
        print("Opção inválida. Tente novamente.")
        print()
