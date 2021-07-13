import matplotlib.pyplot as plt
import numpy as np

# 生成数据
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
# y = [224, 79, 46, 33, 37, 23, 22, 12, 12, 6, 7, 7, 4, 2, 2, 2, 1, 2, 1]
x = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 3]
x = [str(i) for i in x]
y = [31, 68, 116, 142, 158, 141, 157, 136, 101, 94, 81, 88, 78, 69, 64, 58, 42, 29, 102, 16]


# 画柱状图
fig, ax = plt.subplots()
fig.set_size_inches(10.5, 10.5)
ax.bar(x, y, tick_label=x)

# 设置横纵轴标题和图标题
ax.set_xlabel('width height ratio')
ax.set_ylabel('bbox numbers')
ax.set_title('training set analysis 2')

# 展示图和保存
# plt.show()
plt.savefig("./figure2.png", format = 'png', dpi=200)

