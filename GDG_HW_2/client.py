import pickle           # 리스트를 바이트로 변환
from socket import *


def create_list():
    return ["김민성", "자동차공학과", "20213196"]


if __name__ == '__main__':
    client_soc = socket(AF_INET, SOCK_STREAM)
    client_soc.connect(('127.0.0.1', 9900))

    client_soc.sendall(pickle.dumps(create_list()))  # 바이트로 변환한 리스트를 서버에게 보냄

    new_dict = pickle.loads(client_soc.recv(1024))   # 서버가 보낸 바이트를 딕셔너리로 변환함
    print(f"\nReceived Dict : {new_dict}")

