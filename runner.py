# This is a sample Python script.
import sys

from constants import COMMANDS

from delivery_optimizer import DeliveryOptimizer


def execute_command(delivery_optimizer, command):
    if command[0] == COMMANDS[0]:
        delivery_optimizer.add_customer(command[1], int(command[2]), int(command[3]))
    elif command[0] == COMMANDS[1]:
        delivery_optimizer.add_driver(command[1], int(command[2]), int(command[3]))
    elif command[0] == COMMANDS[2]:
        delivery_optimizer.add_restaurant(command[1], int(command[2]), int(command[3]))
    elif command[0] == COMMANDS[3]:
        delivery_optimizer.add_order(int(command[1]), int(command[2]))
    elif command[0] == COMMANDS[4]:
        delivery_optimizer.deliver_order(int(command[1]))


def command_mode(delivery_optimizer):
    try:
        command = input().split()
        while command[0] != "exit":
            execute_command(delivery_optimizer, command)
            command = input().split()
    except Exception as err:
        raise err


def file_mode(delivery_optimizer, file_name):
    try:
        with open(file_name) as file:
            commands = file.readlines()
            for command in commands:
                command.replace("\n", '')
                execute_command(delivery_optimizer, command.split(","))
    except Exception as err:
        raise err


if __name__ == '__main__':
    delivery_optimizer = DeliveryOptimizer()
    if len(sys.argv) > 1:
        file_mode(delivery_optimizer, file_name=sys.argv[1])
    else:
        command_mode(delivery_optimizer)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
