numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
	if num == 1:                # 1 - не простое и не составное, пропускаем
		continue
	is_prime = True             # инициализируем флаг
	for divr in range(2, num):  # на 1 делятся все числа, поэтому перебираем с 2 до num-1
		if num % divr == 0:
			is_prime = False    # найден делитель
			break               # больше проверять для этого числа смысла нет, выходим
	if is_prime:
		primes.append(num)      # добавляем в список простых
	else:
		not_primes.append(num)  # добавляем в список составных
print("Primes:", primes)
print("Not Primes:", not_primes)