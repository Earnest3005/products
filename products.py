products = []
while True:
	product_name = input('請輸入商品名稱： ')
	if product_name == 'q':
		break
	product_price = input('請輸入商品價格： ')
	p = []
	p.append(product_name)
	p.append(product_price)
	products.append(p)
print(products)
print(products[0][0])