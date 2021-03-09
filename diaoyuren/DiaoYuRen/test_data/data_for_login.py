success_data = {'name': '登录-正常数据', 'username': '15191776915', 'password': 'lhj13186395673'}
failed_data = [
    {'name': '登录-反向用例-用户名为空', 'username': '', 'password': '654321', 'error_msg': '用户名不能为空！'},
    {'name': '登录-反向用例-用户名错误', 'username': '财友', 'password': '654321', 'error_msg': '登录验证失败，用户不存在！'},
    {'name': '登录-反向用例-用户名正确-密码错误', 'username': '15191776915', 'password': '34354658', 'error_msg': '账号或密码错误'},
    {'name': '登录-反向用例-密码为空', 'username': '32546', 'password': '', 'error_msg': '密码不能为空'}
]