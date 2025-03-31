import pygame


class F310:
    """
    not even specific to the F310 ☠️☠️☠️
    """

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            print("No joysticks found")
            return None
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        self.deadzone = 0.07

    def update(self):
        """
        Call this once per loop
        """
        pygame.event.pump()

    def apply_deadzone(self, value):
        if abs(value) < self.deadzone:
            return 0
        else:
            return value

    # region axes
    def get_hat(self):
        return self.joystick.get_hat(0)

    # def dpad_up(self):
    #     return -1
    #     # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_DPAD_UP)

    # def dpad_down(self):
    #     return -1
    #     # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_DPAD_DOWN)

    # def dpad_left(self):
    #     return -1
    #     # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_DPAD_LEFT)

    # def dpad_right(self):
    #     return -1
    #     # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_DPAD_RIGHT)

    def left_x(self):
        return self.apply_deadzone(self.joystick.get_axis(0))

    def left_y(self):
        """
        Returns positive UP
        """
        return self.apply_deadzone(-self.joystick.get_axis(1))

    def right_x(self):
        return self.apply_deadzone(self.joystick.get_axis(2))

    def right_y(self):
        """
        Returns positive UP
        """
        return self.apply_deadzone(-self.joystick.get_axis(3))

    def left_trigger(self):
        return self.joystick.get_axis(4)

    def right_trigger(self):
        return self.joystick.get_axis(5)

    # endregion axes

    # region buttons
    def a(self):
        return self.joystick.get_button(1)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_A)
        # return self.joystick.get_button(JoystickType.BUTTON_A)

    def b(self):
        return self.joystick.get_button(2)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_B)

    def x(self):
        return self.joystick.get_button(3)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_X)

    def y(self):
        return self.joystick.get_button(4)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_Y)

    def left_bumper(self):
        return self.joystick.get_button(5)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_LEFTSHOULDER)

    def right_bumper(self):
        return self.joystick.get_button(6)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_RIGHTSHOULDER)

    def back(self):
        return self.joystick.get_button(7)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_BACK)

    def start(self):
        return self.joystick.get_button(8)
        # return self.joystick.get_button(pygame.constants.CONTROLLER_BUTTON_START)

    def left_stick_press(self):
        return self.joystick.get_button(
            pygame.constants.CONTROLLER_BUTTON_LEFTSTICK
        )

    def right_stick_press(self):
        return self.joystick.get_button(
            pygame.constants.CONTROLLER_BUTTON_RIGHTSTICK
        )

    # endregion buttons


if __name__ == "__main__":
    import colorama

    controller = F310()

    def make_green_if_true(b):
        return (
            colorama.Fore.GREEN + str(b) + colorama.Fore.RESET if b else str(b)
        )

    def format_ax(x):
        sx = f"{x: 1.2f}"

        if x > 0:
            return colorama.Fore.GREEN + sx + colorama.Fore.RESET
        elif x < 0:
            return colorama.Fore.RED + sx + colorama.Fore.RESET
        else:
            return colorama.Fore.BLUE + sx + colorama.Fore.RESET

    ms = 0
    while True:
        pygame.event.pump()
        output = "| "

        output += f"{format_ax(controller.left_x())}, {format_ax(controller.left_y())}  | "
        output += f"{format_ax(controller.right_x())}, {format_ax(controller.right_y())}  | "
        output += f"{format_ax(controller.left_trigger())} "
        output += f"{format_ax(controller.right_trigger())} "
        output += "| "

        output += f"{make_green_if_true(controller.a())} "
        output += f"{make_green_if_true(controller.b())} "
        output += f"{make_green_if_true(controller.x())} "
        output += f"{make_green_if_true(controller.y())} "
        output += " "
        output += f"{make_green_if_true(controller.left_bumper())} "
        output += f"{make_green_if_true(controller.right_bumper())} "
        output += " "
        output += f"{make_green_if_true(controller.back())} "
        output += f"{make_green_if_true(controller.start())} "
        output += " "
        output += f"{make_green_if_true(controller.left_stick_press())} "
        output += f"{make_green_if_true(controller.right_stick_press())} "
        output += "| "

        hatx, haty = controller.get_hat()
        output += f"{format_ax(hatx)}, {format_ax(haty)} |"

        # output += f"{make_green_if_true(controller.dpad_up())} "
        # output += f"{make_green_if_true(controller.dpad_down())} "
        # output += f"{make_green_if_true(controller.dpad_left())} "
        # output += f"{make_green_if_true(controller.dpad_right())} "
        # output += " |"

        if ms > 75:
            print(output)
            ms = 0

        ms += pygame.time.delay(10)
