"""write a function square_number that
takes in a number and squares it"""
#input " 1"

def square_number(number):
	return number**2



def test_square_number():
	assert square_number(2) == 4
	assert square_number(8) == 64
	assert square_number(10) == 100
	print('code is correct')

test_square_number()
