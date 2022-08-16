# matplotlib
# 그래프를 그리는 모듈

import matplotlib.pyplot as plt #pyplot = 파이썬에서 사용하는 것

# x = range(5) # = (x = 0, 1, 2, 3, 4)
# y = [3, 5, 8, 2, 5]
# plt.bar(x, y, align="center")
# plt.show()

#plt.bar(x, y) x = 위치, y = 높이


#scatter plot. = 점으로 나타냄 (경향성을 보기 좋다.)


#  xticks() = 막대그래프의 각 변량에 이름을 부여
pos = range(4) # 4개 연도를 나타낼 것이다.
years = [2015, 2016, 2017, 2018]
temperatures = [17, 16, 19, 22]
plt.bar(pos, temperatures)
plt.xticks(pos, years)
plt.show()