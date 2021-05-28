def is_even(number):
	return number % 2 == 0
	

def test_is_even():
	assert is_even(2) == True
	assert is_even(3) == False
	assert is_even(8) == True
	assert is_even(100) == True
	assert is_even(101) == False
	print('code is correct')


test_is_even()
