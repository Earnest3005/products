products = []
while True:
	product_name = input('請輸入商品名稱： ')
	if product_name == 'q':
		break
	product_price = input('請輸入商品價格： ')
	products.append([product_name, product_price])
print(products)
print(products[0][0])

for product in products:
	print(product[0], '的價格是', peoduct[1])