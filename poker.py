import random
import time
import sys

card_list=[]
for i in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
	for j in ['S','H','D','C']:
		card=j+str(i)
		card_list.append(card)


def shuffle():
	sys.stdout.flush()
	random.shuffle(card_list)
	print("洗牌完成:")
	


	






def show(card):
	
	color=[]
	size=[]
	for k in range(1,6):
		color.append(str(card[k-1][0:2]))
	for h in range(1,6):
		size5 = str(card[h - 1][2:len(card[h - 1])])
		if size5=='J':
			size5=11
		elif size5=='Q':
			size5=12
		elif size5=='K':
			size5=13
		elif size5=='A':
			size5=1

		size.append(size5)
	size_set=list(set(size))
	while color[0]==color[1]==color[2]==color[3]==color[4]:
		if(max(size)-min(size)==4):
			print("同花顺")
			return 9
			break
		print('同花')
		return 6
		break
	if size == list(set(size)) and max(size) - min(size) == 4:
		print("顺子")
		return 5
	elif len(size) - 1 == len(size_set):
		print("一对")
		return 2
	elif len(size) - 2 == len(size_set):
		for a in range(0,5):
			for b in range(0,3):
				if size[a]==size_set[b]:
					size[a]=0
					size_set[b]=0
		last = [x for x in size if x != 0]
		if last[0]==last[1]:
			print("三条")
			return 4
		else:
			print("两对")
			return 3
	elif len(size) - 3 == len(size_set):
		for a in range(0, 5):
			for b in range(0, 2):
				if size[a] == size_set[b]:
					size[a] = 0
					size_set[b] = 0
		last=[x for x in size if x != 0]
		if last[0] == last[1] == last[2]:
			print("铁支aka四条")
			return 7
	else:
		print("散牌")
		return 1


if __name__ == "__main__":
	print("初始化牌")
	shuffle()
	card1=card_list[0:5]
	card2=card_list[5:10]
	color1=[]
	size1=[]
	for k in range(1,6):
		color1.append(str(card1[k-1][0:2]))
	for h in range(1,6):
		size5 = str(card1[h - 1][2:len(card1[h - 1])])
		if size5=='J':
			size5=11
		elif size5=='Q':
			size5=12
		elif size5=='K':
			size5=13
		elif size5=='A':
			size5=1

		size1.append(size5)
	color2=[]
	size2=[]
	for k in range(1,6):
		color2.append(str(card2[k-1][0:2]))
	for h in range(1,6):
		size5 = str(card2[h - 1][2:len(card2[h - 1])])
		if size5=='J':
			size5=11
		elif size5=='Q':
			size5=12
		elif size5=='K':
			size5=13
		elif size5=='A':
			size5=1

		size2.append(size5)
	print("发给第一个人的牌是:")
	print(card1)
	s1=show(card1)
	print("发给第二个人的牌是:")
	print(card2)
	
	s2=show(card2)
	if(s1>s2):
		print("1胜利")
	elif (s1<s2):
		print("2胜利")
	elif(s1==s2==1):
		if(max(size1)>max(size2)):
			print("1胜利")
		elif(size1==size2):
			print("平局")
		else:
			print("2胜利")
	








