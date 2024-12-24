'''
njupt一键登录脚本
v1.0版本
可以自动识别哪个校园网，并且登录
如果不想暴露明文密码，可以用base64加密之后使用
by rocket 2024.12.24
rocket_mail@qq.com
'''
import requests
import socket
import urllib.parse
#import base64

import subprocess

def get_current_wifi_ssid_windows():
    try:
        result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], 
                               capture_output=True, text=True, check=True)
        output = result.stdout
        for line in output.split('\n'):
            if 'SSID' in line:
                return line.split(': ')[1].strip()
    except Exception as e:
        print("Error:", e)
    return None



def encode_password(password):
    """使用Base64编码密码"""
    # 将字符串转换为字节类型
    password_bytes = password.encode('utf-8')
    # 使用Base64编码
    encoded_bytes = base64.b64encode(password_bytes)
    # 将编码后的字节转换回字符串
    encoded_password = encoded_bytes.decode('utf-8')
    return encoded_password

def decode_password(encoded_password):
    """解码Base64编码的密码"""
    # 将字符串转换为字节类型
    encoded_bytes = encoded_password.encode('utf-8')
    # 使用Base64解码
    decoded_bytes = base64.b64decode(encoded_bytes)
    # 将解码后的字节转换回字符串
    decoded_password = decoded_bytes.decode('utf-8')
    return decoded_password

def get_local_ip():
    """获取本机IP地址"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
    finally:
        sock.close()
    return local_ip

def construct_login_url(username, password,ssid):
    """构造校园网登录URL"""
    base_url = "https://p.njupt.edu.cn:802/eportal/portal/login"
    wlan_user_ip = get_local_ip()
    type = ""
    if ssid == "NJUPT-CMCC":
        type = "@cmcc"
        print("移动校园网")
    elif ssid == "NJUPT-CHINANET":
        type = "@njxy"
        print("电信校园网")
    elif ssid == "NJUPT":
        print("普通计费校园网")
        type = ""
    else:
        print("不是校园网！退出！")
        exit()
    params = {
        'callback': 'dr1003',
        'login_method': '1',
        'user_account': f',0,{username}{type}',
        'user_password': password,
        'wlan_user_ip': wlan_user_ip,
        'wlan_user_ipv6': '',
        'wlan_user_mac': '000000000000',
        'wlan_ac_ip': '',
        'wlan_ac_name': '',
        'jsVersion': '4.1.3',
        'terminal_type': '1',
        'lang': 'zh-cn',
        'v': '4009'
    }

    query_string = urllib.parse.urlencode(params)
    full_url = f"{base_url}?{query_string}"
    return full_url

def login_to_campus_network_with_get(username, password,ssid):
    """使用GET请求登录校园网"""
    url = construct_login_url(username, password,ssid)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(response.text)


#获取wifi名字
ssid = get_current_wifi_ssid_windows()

# 改这里的账号密码
username = "usermane"
password = "password"

login_to_campus_network_with_get(username, password,ssid)
