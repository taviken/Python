""" Server code """

from typing import Callable
import pickle as I_take_  # i'm so immature...
import threading
import socket
import time

HOST = '127.0.0.1'
PORT = 55555
SERVER = 'SERVER'
KILL_SERVER = 'KILL_SERVER'


def _test():
    while True:
        print('Test Target...')
        time.sleep(1)


def _targ(function: Callable, event: threading.Event) -> Callable:
    def wrapper(*args, **kwargs):
        while not event.isSet():
            res = function(*args, **kwargs)
            return res

    return wrapper


class ThreadServerCallable:
    def __init__(self, target: Callable, arguments=()):
        self.target = target
        self.arguments = arguments

    def run(self, event: threading.Event):
        while not event.isSet():
            self.target(*self.arguments)


class ThreadClient:
    def __init__(self, **opts):
        self._recv_bytes = opts.get('receive', 1024)

    def _send_command(self, commands: dict):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(I_take_.dumps(commands, I_take_.HIGHEST_PROTOCOL))
            data = s.recv(1024)
            print(I_take_.loads(data))

    def KillServer(self):
        self._send_command({SERVER: KILL_SERVER})


class ThreadServer:
    def __init__(self, thread_target: Callable, thread_args=(), **opts):
        self.ServerKill = threading.Event()
        self.TaskKill = threading.Event()
        self.target_object = ThreadServerCallable(target=thread_target, arguments=thread_args)
        self.thread = None
        self._recv_bytes_amount = opts.get('receive', 1024)

    def run(self):
        self._start_thread()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('starting server...')
                print('Connected by', addr)
                while not self.ServerKill.isSet():
                    data = conn.recv(self._recv_bytes_amount)
                    if not data:
                        continue
                    commands = I_take_.loads(data)
                    response = self._handle_commands(commands)
                    conn.sendall(response)
        if self.thread is not None:
            self.thread.join()
        print('Server killed')

    def _start_thread(self):
        target = self.target_object.run
        self.thread = threading.Thread(target=target, args=(self.TaskKill,))
        self.thread.start()

    def _handle_commands(self, commands: dict) -> bytes:
        response = {}
        for category, command in commands.items():
            if category == SERVER:
                response.update(self._process_server_command(command))
        return I_take_.dumps(response)

    def _process_server_command(self, command: str):
        if command == KILL_SERVER:
            self.TaskKill.set()
            self.ServerKill.set()
            return {SERVER: 'Server kill acknowledged'}
        else:
            return {}


if __name__ == '__main__':
    s = ThreadServer(thread_target=_test)
    s.run()
