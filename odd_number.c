def is_odd(number):
	return number % 2 != 0


		


print(is_odd(3))


def test_is_odd():
	assert is_odd(2) == False
	assert is_odd(3) == True
	assert is_odd(8) == False
	assert is_odd(100) == False
	assert is_odd(101) == True

	print('code is correct')

test_is_odd()
