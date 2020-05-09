import os
# check file
if os.path.isfile('products.csv'):
	print("There's your file!")
else:
	print("No file exists.")

# read fil 
products =[]
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'product, price' in line:
			continue
		name, price = line.strip().split(',')
		

# input file
while True:
	name = input('Enter the name of product: ')
	if name == 'q':
		break
	price = input('Enter the price: ')
	price = int(price)
	products.append([name, price])
	# p = []
	# p.append(name)
	# p.append(price)
	# products.append(p)

#print each product
for p in products:
	print('The price of', p[0], 'is $', p[1])

# write file
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')