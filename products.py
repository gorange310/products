products =[]

while True:
	name = input('Enter the name of product: ')
	if name == 'q':
		break
	price = input('Enter the price: ')
	products.append([name, price])
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)

#print each product price
for p in products:
	print('The price of', p[0], 'is $', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')