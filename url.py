import socket
import docker


class SockName:
    @staticmethod
    def get_sock_name():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

try:
    filename = r".env"
    text = open(filename).read()
    open(filename, "w+").write(text.replace('IPV4 = http://127.0.0.1:', 'IPV4 = http://'+SockName.get_sock_name()+':'))
except:
    print('Error')

