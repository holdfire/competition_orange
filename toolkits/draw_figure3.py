import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
x = [str(i) for i in x]
y = [7, 487, 525, 295, 157, 89, 64, 55, 56, 34, 2]


# 画柱状图
fig, ax = plt.subplots()
fig.set_size_inches(10.5, 10.5)
ax.bar(x, y, tick_label=x)

# 设置横纵轴标题和图标题
ax.set_xlabel('width ratio')
ax.set_ylabel('bbox numbers')
ax.set_title('training set analysis 3')

# 展示图和保存
# plt.show()
plt.savefig("./figure3.png", format = 'png', dpi=200)

