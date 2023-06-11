from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties


# 绘制饼图时使用中文字体

app = Flask(__name__)

# 指定中文字体
font = FontProperties(fname=r"/libraries/font-apex/2.0/fonts/Font-APEX-Large.ttf")

@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        input_value = float(request.form['input_name'])  # 获取输入值
        # 计算比例
        life_expenses = input_value * 0.55
        savings_investment = input_value * 0.35
        risk_management = input_value * 0.1

        # 绘制饼图
        mpl.rcParams['font.family'] = ['Arial Unicode MS']
        labels = ['生活開支', '儲蓄與投資', '風險管理']
        sizes = [life_expenses, savings_investment, risk_management]
        colors = ['red', 'yellow', 'orange']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        # plt.title('pie')
        

        # 将图表保存为图片文件
        chart_path = './static/chart.png'  # 图表保存路径，相对于当前工作目录
        plt.savefig(chart_path, format='png')
        plt.close()

        return render_template('index.html', result=[life_expenses, savings_investment, risk_management], chart_path=chart_path)

    return render_template('index.html', result=None, chart_path=None)

if __name__ == '__main__':
    app.run()
