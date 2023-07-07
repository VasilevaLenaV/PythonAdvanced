# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
import re

count = 0
bonus = 0
balans = 0
commission = 1.5
MIN_COMMISSION = 30
MAX_COMMISSION = 600
transactions = []

def check_bonus():
    global count

    if count % 3 == 0:
        add_bonus()


def add_bonus():
    global count,bonus,balans

    bonus = balans * 0.03
    balans += bonus
    transactions.append(("bonus", bonus))
    get_bonus(balans)


def get_balans():
    print(f'Ваш баланс: {balans}')


def get_bonus(bonus_amount):
    print(f'Вам начислен бонус - {bonus_amount}. Текущий баланс:{balans}')


def deposit(amount):
    global balans, count, bonus

    if amount % 50 != 0:
        print(f'Внесите купюры, кратные 50')
    else:
        balans += amount
        count += 1
        get_balans()
        check_bonus()

    transactions.append(("deposit", amount))


def withdraw(amount):
    global balans, count, bonus

    fee = (amount / 100 * commission)
    fee = max(fee, MIN_COMMISSION)
    fee = min(fee, MAX_COMMISSION)

    if amount % 50 != 0:
        print(f'Сумма снятия должна быть кратна 50')
    elif (amount + fee) > balans:
        print(f'Не хватает денег для снятия.')

    else:
        balans -= (amount + fee)
        count += 1
        get_balans()
        check_bonus()

    transactions.append(("withdraw", amount))


def check_balance():
    balance = sum(amount for action, amount in transactions if action == "deposit") - sum(
        amount for action, amount in transactions if action == "withdraw")
    return balance


def menu():
    print("""МЕНЮ:\n\tпополнить - 1,\n\tснять - 2\n\tвыйти - 3\n
        """)
    return int(input('Введите выбор:\t'))


def init():
    global balans, tax, bonus
    bonus =0

    if balans >= 5000000:
        tax = balans * 0.1
        balans -= tax
        print(f'Ваш баланс: {balans}. С вас списали налог {tax}')


def main():
    while True:
        init()
        selected = menu()

        match selected:
            case 1:
                deposit(float(input("Внесите деньги: ")))
            case 2:
                withdraw(float(input("Сумма снятия: ")))
            case 3:
                print("Спасибо за использование нашего банкомата!\n")
                break

    if transactions:
        print(f'\nТранзакции:\n{transactions}')
