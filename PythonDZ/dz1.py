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

balans = 0
commission = 1.5
MIN_COMMISSION = 30
MAX_COMMISSION = 600
count = 0
bonus = 0

while True:
    if balans >= 5000000:
        tax = balans * 0.1
        balans -= tax
        print(f'Ваш баланс: {balans}. С вас списали налог {tax}')
    print("""МЕНЮ:
    пополнить - 1,
    снять - 2
    выйти - 3\n
    """)
    operation = int(input())

    match operation:
        case 1:
            top_up = float(input("Внесите деньги: "))
            if top_up % 50 != 0:
                print(f'Ваш баланс: {balans} Внесите купюры, кратные 50')
            else:
                balans += top_up
                count += 1
                print(f'Ваш баланс: {balans}')
                count += 1
                if count % 3 == 0:
                    bonus = balans * 0.03
                    balans += bonus
                    print(f'Вам начислен бонус - {bonus}. Ваш текущий баланс: {balans}.')

        case 2:
            withdraw = float(input("Сумма снятия: "))
            fee = (withdraw / 100 * commission)
            fee = max(fee, MIN_COMMISSION)
            fee = min(fee, MAX_COMMISSION)

            if withdraw % 50 != 0:
                print(f'Ваш баланс - {balans}. Сумма снятия должна быть кратна 50')
            elif (withdraw+fee) > balans:
                print(f'Ваш текущий баланс: {balans}. Не хватает денег для снятия.')

            else:
                balans -= (withdraw + fee)
                count += 1
                if count % 3 == 0:
                    bonus = balans * 0.03
                    balans += bonus
                    print(f'Вам начислен бонус - {bonus}. Ваш текущий баланс: {balans}.')

        case 3:
            print(f'Ваш баланс - {balans}. Вы вышли из меню')
            break
print("Спасибо за использование нашего банкомата!")

