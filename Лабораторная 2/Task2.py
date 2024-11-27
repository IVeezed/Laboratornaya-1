salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0

for month in range(1, months + 1):

    if spend > salary:
        money_capital += spend - salary

    spend *= (1 + increase)

money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)