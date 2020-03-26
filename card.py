import random
card_turple = ('武则天','嬴政','诸葛亮','宫本武藏','李白')
packbag=[]
fg='________________________'
while 1:
	choose = int(input('''
	充值能让你变得更强!
	请选择指令:
	1. 抽卡
	2. 查看背包
	3. 整理背包
	4. 离开
	'''))
	if choose == 1:
		num = int(input('输入抽卡次数:'))
		for i in range(0,num):
			n = random.randint(0,4)
			print('你抽到了:{}'.format(card_turple[n]))
			packbag.append(card_turple[n])
		print('卡已存入背包')
		print(fg)

	if choose == 2:
		if len(packbag) == 0:
			print('背包暂无英雄,快去抽卡吧!')
			print(fg)
		else:
			for i in packbag:
				print(i)
			print(fg)

	if choose == 3:
		if len(packbag) == 0:
			print('背包暂无英雄,快去抽卡吧!')
			print(fg)
		else:
			packbag.sort()
			for i in packbag:
				print(i)
			print(fg)

	if choose == 4:
		break
	
