from enum import Enum

users = []
class Account(Enum):
    USD = "USD"
    KZT = "KZT"
    RUB = "RUB"
    EUR = "EUR"

class BankAccount:
    name: str
    surname: str
    amount: int = 0
    account: Account = 'KZT'

    def __init__(self, name:str, surname:str, account:Account) -> None:
        self.name = name
        self.surname = surname
        self.account = account

    def set_user(self, name: str, surname: str, account: Account) -> None:
        self.name = name
        self.surname = surname
        self.account = account
    def set_amount(self, amount:int):
        self.amount = amount

    def name(self) -> str:
        return self.name
    def surname(self) -> str:
        return self.surname
    def account(self) -> Account:
        return self.account
    def amount(self) -> int:
        return self.amount
    
    def addToBankAccount(self, x:int):
        self.amount += x
        print("Счет успешно пополнен")

    def substractFromBankAccount(self, x:int):
        if self.amount < x:
            print("Недостаточно средств")
        else:
            self.amount -= x
            print("Вы успешно сняли деньги")

    def moneyConversion(self, b):
        a = self.account
        kurs_kzt = {"KZT":1, "RUB":7.53, "USD":470.69, "EUR":496.17}
        kurs_rub = {"RUB":1, "KZT":0.13, "USD":62.52, "EUR":65.90 }
        kurs_usd = {"RUB":0.016, "KZT":0.0021, "USD":1, "EUR":1.05 }
        kurs_eur = {"RUB":0.015, "KZT":0.0020, "USD":0.95, "EUR":1}
        if b == "KZT":
            self.amount *= kurs_kzt[a]
            self.account = "KZT"
        elif b == "RUB":
            self.amount *= kurs_rub[a]
            self.account = "RUB"
        elif b == "USD":
            self.amount *= kurs_usd[a]
            self.account = "USD"
        elif b == "EUR":
            self.amount *= kurs_eur[a]
            self.account = "EUR"

            

    def __repr__(self):
        return f'{self.name} {self.surname} {self.amount} {self.account}'
        


def create_account(name: str, surname: str, amount:int, account: Account) -> BankAccount:
    user = BankAccount(name=name, surname=surname, account=account)
    user.set_amount(amount=amount)
    users.append(user)

    return user

def get_user(name: str, surname: str) -> BankAccount | None:
    user = next((u for u in users if name == u.name and surname == u.surname), None)
    if not user:
        print('User not found')
        return
    return f'{user.name} {user.surname}. Ваш счет: {user.amount} {user.account}'

def delete_user(name: str, surname: str) -> BankAccount | None:
    user = next((u for u in users if name == u.name and surname == u.surname), None)
    if not user:
        print('User not found')
        return
    users.remove(user)
    print("Пользователь удален")

fake_account = BankAccount(name="Mark", surname="Doe", account="RUB")

fake_account.amount = 1500
users.append(fake_account)

d = {"1":"KZT", "2":"RUB", "3":"USD", "4":"EUR"}
while(True):
    inp = input("Выберите действие: \n 1. Создание пользователя \n 2. Выбрать пользователя \n 3. Удалить пользователя \n 0. Выход \n")
    if inp == '0':
        break
    elif inp == "1":
        name = input("Введите имя: ")
        surname = input("Введите фмаилия: ")
        v = input("Выберите курс валют: \n 1. KZT \n 2. RUB \n 3. USD \n 4. EUR \n")
        account = d[v]
        user = create_account(name=name, surname=surname, account=account, amount=0)
        print("Ваш аккаунт создан. ")
    elif inp == '2':
        name = input("Введите имя: ")
        surname = input("Введите фмаилия: ")
        print(get_user(name=name, surname=surname))
        while(True):
            inp2 = input("Выберите операцию: \n 1. Добавить на счет \n 2. Снять деньги \n 3. Сконвертировать \n 0. Назад\n")
            if inp2 == "0":
                break
            elif inp2 == "1":
                x = int(input("Введите суммy: \n"))
                user.addToBankAccount(x)
                print(get_user(name=name, surname=surname))
            elif inp2 == "2":
                x = int(input("Введите суммy: \n"))
                user.substractFromBankAccount(x)
                print(get_user(name=name, surname=surname))
            elif inp2 == "3":
                b = input("Выберите курс валют: \n 1. KZT \n 2. RUB \n 3. USD \n 4. EUR \n")
                account = d[b]
                user.moneyConversion(account)
                print(get_user(name=name, surname=surname))
    elif inp == "3":
        name = input("Введите имя: ")
        surname = input("Введите фмаилия: ")
        delete_user(name=name, surname=surname)



            




