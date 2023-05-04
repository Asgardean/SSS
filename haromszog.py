#haromszog
a = int(input("Add meg a háromszög A oldalát"))
b = int(input("Add meg a háromszög B oldalát"))
c = int(input("Add meg a háromszög C oldalát"))
if c < a+b and a < b+c and b<a+c:
	print('A(z)', a, ',', b, 'és', c, 'háromszöget alkot')
else:
	print('A(z)', a, ',', b, 'és', c, 'nem alkot háromszöget')


