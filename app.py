from flask import Flask, render_template, request, redirect, flash
from data import salary_list
from user_data import user_list

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

# 登录模块
@app.route('/login', methods=["POST"])
def hello_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    for user in user_list:
        if username == user['username'] and password == user['password']:
            return render_template('admin.html', salary_list=salary_list)
        else:
            flash('登录失败，用户名或密码错误！')
            return redirect('/login')

# 删除模块
@app.route('/delete/<name>')
def hello_delete(name):  # put application's code here
    for salary in salary_list:
        if salary['name'] == name:
            salary_list.remove(salary)
    return render_template('admin.html',
                           salary_list=salary_list)

# 修改模块 选择先调用删除再调用添加模块
@app.route('/change/<name>')
def hello_change(name):  # put application's code here
    for salary in salary_list:
        if salary['name'] == name:
            return render_template('change.html',
                                   user=salary)

    return render_template('admin.html',
                           salary_list=salary_list)

# 修改模块
@app.route('/changed/<name>', methods=["POST"])
def hello_changed(name):
    for salary in salary_list:
        if salary['name'] == name:
            salary['name'] = request.form.get('name')
            salary['department'] = request.form.get('department')
            salary['position'] = request.form.get('position')
            salary['salary'] = request.form.get('salary')

    return render_template('admin.html',
                           salary_list=salary_list)

# 跳转至添加界面
@app.route('/add')
def hello_add():
    return render_template('add.html')

# 添加模块
@app.route('/add2', methods=['POST'])
def hello_add2():
    salary = {}
    salary['name'] = request.form.get('name')
    salary['department'] = request.form.get('department')
    salary['position'] = request.form.get('position')
    salary['salary'] = request.form.get('salary')
    salary_list.insert(0, salary)
    return render_template('admin.html',
                           salary_list=salary_list)

if __name__ == '__main__':
    app.run()