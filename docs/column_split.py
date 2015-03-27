
with open('list.csv') as original_list:
	with open('new_list.csv', 'w') as new_list:
		for row in original_list:
			new_list.write('","'.join(row.split(' ')))
original_list.close()
new_list.close()
