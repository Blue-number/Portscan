from dataclasses import dataclass
from datetime import datetime
from multiprocessing.pool import ThreadPool
import socket
from threading import Thread

from py import process
class ScanPort:
    def __init__(self):
        self.ip = None
 
    def scan_port(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = s.connect_ex((self.ip, port))
            if res == 0:  # 端口开启
                print('{} is opening \r'.format(port))
                print("\n")
            else:
                print('{}: no\n'.format(port))
        except Exception as e:
            print(e)
        finally:
            s.close()
 
    def start(self):
        remote_server = input("输入要扫描的远程主机:")
        self.ip = socket.gethostbyname(remote_server)
        ports = [i for i in range(20, 30)]
        socket.setdefaulttimeout(0.5)
        # 开始时间
        t1 = datetime.now()
        # 设置多进程
        threads = []
        pool = ThreadPool(processes=8)
        pool.map(self.scan_port, ports)
        pool.close()
        pool.join()
 
        print('端口扫描已完成，耗时：', datetime.now() - t1)
 
 
ScanPort().start()


