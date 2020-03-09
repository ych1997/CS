choose='0'
year=int(input("請輸入年份: "))
"""
print(year%400)
print(year%100)
print(year%4)
"""
while(year<0 or choose=='0'):
	if year<0:
		print("輸入有誤，請重新輸入！")
		year=int(input("請輸入年份: "))
	else:
		if year%400==0 :
			print("閏年")
		elif year%100==0 and year%400!=0:
			print("平年")
		elif year%100!=0 and year%4==0:
			print("閏年")
		else:
			print("平年")
		choose=input("輸入0為繼續，其他則結束")
		if choose=='0':
			year=int(input("請輸入年份: "))