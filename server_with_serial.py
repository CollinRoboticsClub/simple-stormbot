import socket, serial

PORT = 12345  # Port to listen on (non-privileged ports are > 1023)
ser = serial.Serial("COM13", baudrate=115200)
# ser.write(bytes([127, 127, 127, 127, 127]) + b"\n")
# exit()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(f"Client sent: {data!r}")

            ser.write(data)
            # ser.write(bytes([127, 255, 127, 255, 255]) + b"\n")
            # print(ser.readline())

            # conn.sendall(data + b" as well :)")
