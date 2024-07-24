import socket


def test_client():
    server_ip = '127.0.0.1'  # Use the IP address of the machine running the server
    server_port = 12345       # Make sure this matches the server port

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Send a test message
    client_socket.send("Hello from client".encode('utf-8'))

    # Close the connection
    client_socket.close()


if __name__ == "__main__":
    test_client()
