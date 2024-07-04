from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置 Flask 应用的秘密密钥

# 模拟数据库，存储用户信息
users = {'admin': {'password': 'secret'}}  # 用户名为 admin，密码为 secret

# Flask-Login 需要一个 LoginManager 实例来管理登录状态
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # 设置登录页面的视图函数名为 login

# 定义一个用户类，继承自 UserMixin，用于加载用户对象
class User(UserMixin):
    def __init__(self, username):
        self.id = username

# 加载用户的回调函数，接收用户标识符并返回用户对象
@login_manager.user_loader
def load_user(username):
    if username not in users:
        return None
    return User(username)

# 定义首页视图函数，使用 @login_required 装饰器保护页面，只有登录用户才能访问
@app.route('/')
@login_required
def index():
    return render_template('index.html', username=current_user.id)

# 定义登录页面视图函数
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # 处理 POST 请求，即用户提交登录表单
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:  # 验证用户名和密码
            user = User(username)
            login_user(user)  # 登录用户
            return redirect(url_for('index'))  # 登录成功，重定向到首页
        else:
            flash('Invalid username or password')  # 登录失败，显示错误消息

    return render_template('login.html')  # GET 请求时，渲染登录页面模板

# 定义登出页面视图函数
@app.route('/logout')
@login_required
def logout():
    logout_user()  # 登出用户
    return redirect(url_for('login'))  # 重定向到登录页面

if __name__ == '__main__':
    app.run(debug=True)  # 在调试模式下运行 Flask 应用
