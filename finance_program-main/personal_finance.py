from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import io
import base64

personal_finance = Flask(__name__)

@personal_finance.route('/budget_management', methods=['GET', 'POST'])
def budget_management():
    if request.method == 'POST':
        # 處理使用者提交的预算管理表單數據
        # 实现预算管理功能的逻辑
        # 数据
        salary=int(input())
        labels = ['生活支出', '儲蓄與投資', '風險管理']
        sizes = [55, 35, 10]

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


if __name__ == '__main__':
    personal_finance.run()
