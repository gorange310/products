import os
# check file and read file
products =[]
if os.path.isfile('products.csv'):
	print("There's your file!")
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print("No file exists.")
		
# user inputs file
while True:
	name = input('Enter the name of product: ')
	if name == 'q':
		break
	price = input('Enter the price: ')
	price = int(price)
	products.append([name,price])

# print each product
for p in products:
	print('The price of', p[0], 'is $', p[1])

# write file
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')