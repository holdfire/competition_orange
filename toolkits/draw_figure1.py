import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
y = [224, 79, 46, 33, 37, 23, 22, 12, 12, 6, 7, 7, 4, 2, 2, 2, 1, 2, 1]


# 画柱状图
fig, ax = plt.subplots()
fig.set_size_inches(10.5, 10.5)
ax.bar(x, y, tick_label=x)

# 设置横纵轴标题和图标题
ax.set_xlabel('bbox numbers')
ax.set_ylabel('images numbers')
ax.set_title('training set analysis')

# 展示图和保存
# plt.show()
plt.savefig("./figure1.png", format = 'png', dpi=200)

