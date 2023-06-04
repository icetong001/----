import matplotlib.pyplot as plt

# 数据
labels = ['Apple', 'Banana', 'Orange']
sizes = [30, 40, 20]
colors = ['red', 'yellow', 'orange']

# 绘制饼图
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Fruit Distribution')

# 显示图表
#plt.show()

# 将图表保存为图片文件
chart_path = './static/chart.png'  # 图表保存路径，相对于当前工作目录
plt.savefig(chart_path, format='png')
plt.close()