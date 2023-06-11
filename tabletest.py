from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('tabletest.html')

@app.route('/result', methods=['POST'])
def result():
    user_input = request.form['input_name']

    return render_template('tabletest_2.html', user_input=user_input)

# @app.route('/result', methods=['POST'])
# def localplace():
#     localplace = request.form['localplace']

#     return render_template('tabletest.html', localplaceç=localplace)
if __name__ == '__main__':
    app.run()