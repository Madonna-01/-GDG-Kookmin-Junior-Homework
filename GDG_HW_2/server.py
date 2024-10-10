import pickle
from socket import *   # socket을 사용할 때 socket.을 붙이지 않아도 됨


def list_to_dict(dict_values):                  # 인자로 받은 리스트를 딕셔너리로 변환
    dict_keys = ["이름", "학과", "학번"]

    return dict(zip(dict_keys, dict_values))


if __name__ == '__main__':
    server_soc = socket(AF_INET, SOCK_STREAM)       # 인자로 AF(주소 체계)와 소켓 타입을 입력 받음
    server_soc.bind(('', 9900))                     # 튜플 형식으로 입력 받음
    server_soc.listen(1)                            # 하나의 클라이언트만 받음

    (client_soc, addr) = server_soc.accept()        # 튜플 형식으로 반환함

    new_list = pickle.loads(client_soc.recv(1024))  # 클라이언트에서 받은 바이트를 리스트로 변환함
    print(f"\nReceived List : {new_list}")

    client_soc.sendall(pickle.dumps(list_to_dict(new_list))) # 바이트로 변환해서 클라이언트에게 보냄
