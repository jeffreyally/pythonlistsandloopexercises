incoming_ajax_data = [
	{ "name": 'Mario', "last_name": 'Montes' },
	{ "name": 'Joe', "last_name": 'Biden' },
	{ "name": 'Bill', "last_name": 'Clon' },
	{ "name": 'Hilary', "last_name": 'Mccafee' },
	{ "name": 'Bobby', "last_name": 'Mc birth' }
]

#Your code go here:
def data_transformer(data):
	listofnames = []
	for items in data:
		listofnames.append(items['name']+' '+items['last_name'])
		
	return listofnames

print(data_transformer(incoming_ajax_data))
