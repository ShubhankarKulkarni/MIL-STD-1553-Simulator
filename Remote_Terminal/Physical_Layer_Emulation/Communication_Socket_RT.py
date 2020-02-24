import socket
import threading


class RT_Sender:

    def send_message(self, message):
        destination_ip = "255.255.255.255"
        destination_port = 2000
        socket_variable = \
            socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        socket_variable.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        socket_variable.sendto(message, (destination_ip, destination_port))


class RT_Listener:

    import socket

    data_received = list()

    def start_listening(self):
        port = 2001
        socket_variable = \
            socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        socket_variable.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        socket_variable.bind(("", port))
        while True:
            data, addr = socket_variable.recvfrom(1024)
            self.data_received.append(str(data))


if __name__ == "__main__":
    listener = RT_Listener()
    listener_thread = threading.Thread(
        target=listener.start_listening)
    listener_thread.start()
    while True:
        if listener.data_received:
            print(listener.data_received)
            listener.data_received = ""
