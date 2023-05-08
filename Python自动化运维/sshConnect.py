""" 
  作   者：胡晨曦
  开发时间：2023/5/7 21:32
  功   能：用SSH连接网络设备
"""
import paramiko
import time

Channel = paramiko.SSHClient()
# 如果再生产环境下应当使用更加严格的策略，如WarningPolicy()或RejectPolicy()。
Channel.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# invoke_shell()将启动一个连接到SSH服务器的交互式shell会话。在调用该函数时可以传入一些其他参数（如终端类型、宽度、高度等）。
# hostname:目标主机ip地址，username:用户名，password:用户密码
Channel.connect(hostname="192.168.20.128", username='root',
                password='123456', look_for_keys=False, allow_agent=False)
# 拿到shell
shell = Channel.invoke_shell()
# 执行shell命令,可以再里面添加需要的shell命令输入结束记得加上 \n 相当于按回车
shell.send()
# 等待命令执行完成
time.sleep(2)
# 获取终端输出结果
output = shell.recv(65535).decode("utf-8")
print(output)
Channel.close()

