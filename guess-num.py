# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random

count = 0
start = input('請決定隨機數字範圍開始值:')
end = input('請決定隨機數字範圍結束值:')
start = int(start)
end = int(end)
r = random.randint(start,end)

while True:
	count += 1
	num = input('請輸入數字:')
	num = int(num)
	print('這是你猜的第', count,'次')
	if r == num:
		print('你猜中了!')
		break
	elif r > num:
		print('您猜的數字比答案小')
	elif r < num:
		print('您猜的數字比答案大')