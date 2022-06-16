products = []
while True:
	product_name = input('請輸入商品名稱： ')
	if product_name == 'quit':
		break
	product_price = input('請輸入商品價格： ')
	products.append([product_name, product_price])

for product in products:
	print(product[0], '的價格是', product[1])

with open('products.csv', 'w') as f:
	f.write('商品,價格\n')
	for product in products:
		f.write(product[0] + ',' + product[1] + '\n') 