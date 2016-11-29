
class NetDevice(object):
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

        self.serial_number = ''
        self.vendor = ''
        self.model = ''
        self.os_version = ''
        self.uptime = ''

myobj1 = NetDevice(ip_addr='1.1.1.1', username='admin', password='pwd')
myobj2 = NetDevice(ip_addr='1.1.1.2', username='admin', password='pwd')
myobj3 = NetDevice(ip_addr='1.1.1.3', username='admin', password='pwd')
myobj4 = NetDevice(ip_addr='1.1.1.4', username='admin', password='pwd')

