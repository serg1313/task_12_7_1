per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Укажите сумма вклада "))
rate = list(per_cent.values())
deposit = list(map(lambda x : int(x*money/100), rate))
deposit.sort()
print("Максимальная сумма, которую вы можете заработать " + str(deposit[-1]))