def sum(a, b):
	return a + b
	
def test_sum_numbers():
	assert sum_numbers(3, 4) == 7
	assert sum_numbers(1, 2) == 3
	assert sum_numbers(2, 2) == 4
	assert sum_numbers(1, 3) == 4
	
def test_sum_numbers2():
	assert sum_numbers(1, 2) == 3
	assert sum_numbers(2, 2) == 4
