#My implementation of FizzBuzz

fizz = "Fizz"
buzz = "Buzz"

for i in range(100):
	if i % 3 == 0 and i % 5 == 0:
		print(fizz+buzz)
	elif i % 3 == 0:
		print(fizz)
	elif i % 5 == 0:
		print(buzz)
	else:
		print(i)