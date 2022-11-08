#登录页元素定位

class Login_locations:
    account_Login = ("xpath","//span[@class='login_way login_by_mima']")
    user = ("xpath","//input[@placeholder='请输入账号']")
    pwd = ("xpath","//input[@placeholder='输入密码']")
    btn_login = ("xpath","//*[@class='login_btn']/a")