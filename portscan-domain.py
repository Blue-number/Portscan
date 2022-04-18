




from email import parser
from multiprocessing.pool import ThreadPool
import optparse
from socket import gethostbyaddr, socket
from threading import Thread
from py import process
from requests import options

from yaml import parse


Port = [80,21,23,22,25,110,443,1080,3306,3389,1521,1433]
Server = ['HTTP','FTP','TELNET','SSH','SMTP','POP3','HTTPS','SOCKS','MYSQL','Misrosoft RDP','Oracle','Sql Server']

def Scan(tghost,tgport,Server):
    try:
        s = socket()
        s.connect(tghost,tgport)
        print(tghost + '______>' + str(tgport) + ' open',end = '||||| ')
        print(str(tgport) + '------>' + Server)
        s.close()
    except:
        print(str(tgport) + '------>' + 'not open')

def hostToddr(host):  #将域名转换成Ip
    try:
        return gethostbyaddr(host)
    except:
        return
def main():
    parser = optparse.OptionParser()
    parser.add_option('-t', dest = 'dname')
    #parser.add_option('-p',dest = 'pname')
    (options,args)=parser.parse_args()

    if(options.dname==None):
        print('[-] you must specify a target host and port')
        exit(0)
    else:
        tgname = options.dname
    ip = hostToddr(tgname)
    #Scan(ip)
    for i,j in zip(Port,Server): #用线程提高速度
        t = Thread(target = Scan,args = (ip,i,j))
        t.start()
    input()#cmd界面如果快速闪退，请加入这条代码
if __name__ == '__main__':
    main()
