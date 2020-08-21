# 輸入商品及價錢
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')	
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格', p[1])

# 打開檔案
with open('products.csv','w') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')