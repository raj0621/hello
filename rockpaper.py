from random import randint
# print("Rock")
# print("Paper")
# print("Scissor")

for x in range(1,10):
	player=input("Choose your choice....").lower()
	rand_num=randint(0,2)
	if randint==0:
		computer="rock"
	elif randint==1:
		computer="paper"
	else:
		computer="scissor"
	print(f"Computer plays {computer}")

	if player==computer:
		print("it s tie...")
	elif player=="rock":
		if computer=="Scissor":
			print("player wins....")
		else:
			print("computer wins")
	elif player=="scissor":
		if computer=="paper":
			print("player wins....")
		else:
			print("computer wins")
	elif player=="paper":
		if computer=="rock":
			print("player wins....")
		else:
			print("computer wins")
	else:
		print("something wrong input by player")
