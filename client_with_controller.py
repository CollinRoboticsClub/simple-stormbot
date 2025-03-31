import socket
import time

from f310 import F310

# HOST = "127.0.0.1"  # The server's hostname or IP address
HOST = "romi.local"  # The server's hostname or IP address
PORT = 12345  # The port used by the server


def map(
    val: float, in_min: float, in_max: float, out_min: float, out_max: float
) -> float:
    return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def main():
    controller = F310()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # msg = ""
        # while msg != "exit":
        #     msg = input("Enter message to send to server: ")
        #     s.sendall(msg.encode())

        #     data = s.recv(1024)
        #     print(f"Server sent back: {data.decode()}")

        # while True:
        #     msg = bytes([127, 127, 127]) + b"\n"
        #     s.sendall(msg)
        #     print(("Sent: " + ", ".join([f"{b:2}" for b in msg.strip()])).ljust(25))
        #     time.sleep(0.1)

        while not controller.back():
            controller.update()

            if controller.a():
                intake = 230
            elif controller.b():
                intake = 20
            else:
                intake = 127

            if controller.x():
                magazine = 230
            elif controller.y():
                magazine = 20
            else:
                magazine = 127

            # x = int(map(controller.left_x(), -1.0, 1.0, 0, 255))
            # y = int(map(controller.left_y(), -1.0, 1.0, 0, 255))
            # rotation = int(map(controller.right_x(), -1.0, 1.0, 0, 255))
            left = int(map(controller.left_y(), -1.0, 1.0, 0, 255))
            right = int(map(controller.right_y(), -1.0, 1.0, 0, 255))
            # middle = int(map(controller.right_x(), -1.0, 1.0, 0, 255))
            middle = 127

            # msg = bytes([x, y, rotation, intake, magazine]) + b"\n"
            msg = bytes([left, right, middle, intake, magazine]) + b"\n"
            # msg = bytes([x, y, rotation]) + b"\n" # use struct.unpack or something idk

            s.sendall(msg)

            # resp = s.recv(1024)

            print(
                ("Sent: " + ", ".join([f"{b:2}" for b in msg.strip()])).ljust(
                    25
                ),
                # f"Response: {resp.decode().strip()}".ljust(25),
                # f" FPS: {clock.get_fps():.2f}",
            )

            time.sleep(0.100)
            # time.sleep(0.5)


if __name__ == "__main__":
    main()
