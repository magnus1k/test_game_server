# coding:utf8


from socket import AF_INET, SOCK_STREAM, socket
import struct


def send_data(sendstr, command_id):
    head_0 = chr(0)  # 协议头0
    head_1 = chr(0)  # 协议头1
    head_2 = chr(0)  # 协议头2
    head_3 = chr(0)  # 协议头3
    proto_version = chr(0)  # 协议头版本号
    server_version = 0  # 服务器版本号
    sendstr = sendstr

    data = struct.pack('!sssss3I', head_0, head_1, head_2, head_3,
                       proto_version, server_version, len(sendstr) + 4, command_id)

    senddata = data + sendstr
    return senddata

if __name__ == '__main__':
    HOST = "magnus1k.com"  # 服务端地址
    PORT = 1000  # 服务端端口
    ADDR = (HOST, PORT)

    client = socket(AF_INET, SOCK_STREAM)  # 创建socket，TCP
    client.connect(ADDR)  # 连接服务器
    client.sendall(send_data('Hello Server', 1))  # 发送数据给服务器
    client.sendall(send_data('Bye Server', 2))  # 发送数据给服务器
    # while True:
    #     pass
