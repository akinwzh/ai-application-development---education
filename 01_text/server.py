from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # 添加这行
import os

app = Flask(__name__)
CORS(app)  # 添加这行

# 用户数据文件路径
USERS_FILE = 'users.txt'

# 确保用户文件存在
if not os.path.exists(USERS_FILE):
    open(USERS_FILE, 'w').close()

# 注册路由
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'success': False, 'message': '请填写所有必填字段'}), 400

    # 检查用户名是否已存在
    with open(USERS_FILE, 'r') as f:
        for line in f:
            stored_username, stored_email, _ = line.strip().split(',')
            if stored_username == username or stored_email == email:
                return jsonify({'success': False, 'message': '用户名或邮箱已存在'}), 400

    # 存储新用户
    with open(USERS_FILE, 'a') as f:
        f.write(f"{username},{email},{password}\n")

    return jsonify({'success': True, 'message': '注册成功'}), 201

# 登录路由
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print("Received login data:", data)  # 添加这行
    username_or_email = data.get('username')
    password = data.get('password')

    if not username_or_email or not password:
        return jsonify({'success': False, 'message': '请填写所有必填字段'}), 400

    # 验证用户
    with open(USERS_FILE, 'r') as f:
        for line in f:
            try:
                stored_data = line.strip().split(',')
                if len(stored_data) != 3:
                    continue  # 跳过格式不正确的行
                stored_username, stored_email, stored_password = stored_data
                if (stored_username == username_or_email or stored_email == username_or_email) and stored_password == password:
                    return jsonify({'success': True, 'message': '登录成功', 'username': stored_username}), 200
            except ValueError:
                continue  # 如果行格式不正确，跳过这一行

    return jsonify({'success': False, 'message': '用户名/邮箱或密码错误'}), 401

# 静态文件路由
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)