from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import os
import io
import base64

personal_finance = Flask(__name__)

# 路徑和視覺圖的函数
@personal_finance.route('/')


def index():
    # 数据
    labels = ['A', 'B', 'C', 'D']
    sizes = [30, 40, 10, 20]

    # 生成饼图
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()
    # 将图表保存为图片文件
    chart_path = 'static/chart.png'  # 定义图表保存路径
    plt.savefig(chart_path, format='png')
    plt.close(fig)

    # 渲染 HTML 模板并传递图表路径
    return render_template('budget_management.html', chart_path=chart_path)


@personal_finance.route('/budget_management', methods=['GET', 'POST'])
def budget_management():
    if request.method == 'POST':
        # 處理使用者提交的预算管理表單數據
        # 实现预算管理功能的逻辑
        # 数据
        labels = ['A', 'B', 'C', 'D']
        sizes = [30, 40, 10, 20]

        # 生成饼图
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.axis('equal')

        # 保存图表为临时文件
        chart_path = 'static/chart.png'
        plt.savefig(chart_path)        
        return render_template('budget_management.html', chart_path=chart_path)
    else:
        return render_template('budget_management.html', chart_path=chart_path)

@personal_finance.route('/expense_tracking', methods=['GET', 'POST'])
def expense_tracking():
    if request.method == 'POST':
        # 处理用户提交的支出追踪表单数据
        # 实现支出追踪功能的逻辑

        return render_template('expense_tracking.html')
    else:
        return render_template('expense_tracking.html')

@personal_finance.route('/credit_card_expenses', methods=['GET', 'POST'])
def credit_card_expenses():
    if request.method == 'POST':
        # 处理用户提交的信用卡月支出表单数据
        # 实现信用卡月支出功能的逻辑

        return render_template('credit_card_expenses.html')
    else:
        return render_template('credit_card_expenses.html')

@personal_finance.route('/account_summary', methods=['GET', 'POST'])
def account_summary():
    if request.method == 'POST':
        # 处理用户提交的账户信息表单数据
        # 实现账户信息功能的逻辑

        return render_template('account_summary.html')
    else:
        return render_template('account_summary.html')
def generate_pie_chart():
    # 生成圆饼图
    # 数据
    labels = ['Apple', 'Banana', 'Orange']
    sizes = [30, 40, 20]
    colors = ['red', 'yellow', 'orange']

    # 绘制饼图
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
    plt.title('Fruit Distribution')

    # 显示图表
    plt.show()


if __name__ == '__main__':
    personal_finance.run()
