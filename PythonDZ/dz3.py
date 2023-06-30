from fractions import Fraction


def add_fractions(numerator_a, denominator_a, numerator_b, denominator_b):
    common_denominator = denominator_a * denominator_b
    sum_numerator = (numerator_a * denominator_b) + (numerator_b * denominator_a)
    return f"{sum_numerator}/{common_denominator}"


def multiply_fractions(numerator_a, denominator_a, numerator_b, denominator_b):
    multiply_numerator = numerator_a * numerator_b
    multiply_denominator = denominator_a * denominator_b

    return f"{multiply_numerator}/{multiply_denominator}"



fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

numerator1, denominator1 = map(int, fraction1.split('/'))
numerator2, denominator2 = map(int, fraction2.split('/'))

sum_fraction = add_fractions(numerator1, denominator1, numerator2, denominator2)
product_fraction = multiply_fractions(numerator1, denominator1, numerator2, denominator2)

print(f"Сумма дробей: {sum_fraction}")
print(f"Произведение дробей: {product_fraction}")

#Fraction
fraction1 = Fraction(numerator1, denominator1)
fraction2 = Fraction(numerator2, denominator2)
print(f"Проверка Fraction")
print(f"Сумма дробей: {fraction1 + fraction2}")
print(f"Произведение дробей: {fraction1 * fraction2}")