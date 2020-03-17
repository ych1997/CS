import random 
choose1=input("0是石頭，2是剪刀，5是布，請輸入： ")
player1=0
player2=0
choose2=-2
while (choose1!='0' and choose1!='2' and choose1!='5'):
	choose1=input("輸入有誤，請重新輸入！\n0是石頭，2是剪刀，5是布，請輸入： ")

while (player1!=8 and player2!=8):
	choose1=int(choose1)
	temp=random.randint(0,2)
	if temp==0:
		print("玩家2出石頭")
		choose2=0
	elif temp==1:
		print("玩家2出剪刀")
		choose2=2
	elif temp==2:
		print("玩家2出布")
		choose2=5

	if choose1==choose2:
		print("平手")
	elif (choose1==0 and choose2==2) or (choose1==2 and choose2==5) or (choose1==5 and choose2==0):
		print("玩家1獲得兩分！")
		player1+=2
	elif (choose2==0 and choose1==2) or (choose2==2 and choose1==5) or (choose2==5 and choose1==0):	
		print("玩家2獲得兩分！")
		player2+=2
	if player1==8:
		print("玩家1獲勝！\n")
	elif player2==8:
		print("玩家2獲勝！\n")
	else:
		print("玩家1現在分數："+str(player1)+"，"+"玩家2現在分數："+str(player2)+"\n")
		print("*******************************************************\n")
		choose1=input("0是石頭，2是剪刀，5是布，請輸入： ")
		while (choose1!='0' and choose1!='2' and choose1!='5'):
			choose1=input("輸入有誤，請重新輸入！\n0是石頭，2是剪刀，5是布，請輸入： ")
	

