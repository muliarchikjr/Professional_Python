import socket

# IP-адрес и порт сервера
SERVER_HOST = "192.168.1.100"
SERVER_PORT = 7777


def send_request(command, login, password):
    """Функция отправляет команду на сервер"""
    message = f"command:{command}; login:{login}; password:{password}"

    # Создаём сокет
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Подключаемся к серверу
        client.connect((SERVER_HOST, SERVER_PORT))

        # Отправляем данные
        client.send(message.encode())

        # Получаем ответ от сервера
        response = client.recv(1024).decode()
        print(f"Ответ сервера: {response}")

    except ConnectionRefusedError:
        print("Ошибка: Не удалось подключиться к серверу!")
    finally:
        client.close()  # Закрываем соединение


# Регистрация пользователей
send_request("reg", "user1", "password123")
send_request("reg", "user2", "qwerty456")
send_request("reg", "user3", "hello789")

# Вход пользователей
send_request("signin", "user1", "password123")
send_request("signin", "user2", "qwerty456")
send_request("signin", "user3", "hello789")