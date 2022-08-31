'''
'''

from commands import commands
from coordinate import Coordinate, coordinates

from utils import check_type, check_if_dir_valid, replace_address, replace_word

class Motor():
    # Public variables.
    controller = None

    # Private variables.
    __request_ID = None
    __address = None        # uint
    __steps = None
    __limit = None
    __IO = None
    __velocity = None
    __commands = commands['motor']

    def __init__(self, controller):
        self.controller = controller

    def home(self, address):
        # Check the address type.
        check_type(address, int)
        # Get the home command.
        command = self.__commands['home']
        # Replace 'address' with the desired address. 
        command = replace_address(command, address)
        # Send the command.
        self.controller.write(command)

    def mrel(self, address, steps, velocity):
        # Check the input types.
        check_type(address, int)
        check_type(steps, int)
        check_type(velocity, int)
        # Get the mrel command.
        command = self.__commands['mrel']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'steps', steps)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def mabs(self, address, steps, velocity):
        # Check the input types.
        check_type(address, int)
        check_type(steps, int)
        check_type(velocity, int)
        # Get the mabs command.
        command = self.__commands['mabs']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'steps', steps)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def mlim(self, address, limit, velocity):
        # Check the input types.
        check_type(address, int)
        check_type(limit, int)
        check_type(velocity, int)
        # Get the mlim command.
        command = self.__commands['mlim']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'limit', limit)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def mgp(self, address, IO, velocity):
        # Check the input types.
        check_type(address, int)
        check_type(IO, int)
        check_type(velocity, int)
        # Get the mgp command.
        command = self.__commands['mgp']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Replace 'steps' with the desired steps.
        command = replace_word(command, 'IO', IO)
        # Replace 'velocity' with the desired velocity.
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def qpos(self, address):
        # Check the input types.
        check_type(address, int)
        # Get the ?pos command.
        command = self.__commands['?pos']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Send the command.
        self.controller.write(command)

    def qmv(self, address):
        # Check the input types.
        check_type(address, int)
        # Get the ?mv command.
        command = self.__commands['?mv']
        # Replace 'address' with the desired address.
        command = replace_address(command, address)
        # Send the command.
        self.controller.write(command)

    def hdir(self, address, direction):
        # Check the direction if valid.
        check_type(address, int)
        check_type(direction, int)
        check_if_dir_valid(direction)
        # Get the command.
        command = replace_address(self.__commands['hdir'], address)
        command = replace_word(command, 'direction', direction)
        # Send the command.
        self.controller.write(command)
    
    def hvel(self, address, velocity):
        # Check validity.
        check_type(address, int)
        check_type(velocity, int)
        # Get the command.
        command = replace_address(self.__commands['hvel'], address)
        command = replace_word(command, 'velocity', velocity)
        # Send the command.
        self.controller.write(command)

    def hpol(self, address, polarity):
        # Check validity.
        check_type(address, int)
        check_type(polarity, int)
        # Get the command.
        command = replace_word(self.__commands['hpol'], 'polarity', polarity)
        # Send the command.
        self.controller.write(command)

    def tout(Self, address, milliseconds):
        return None

    def gppol(self, address, polarity):
        return None

    def stop(self, address):
        # Check validity.
        check_type(address, int)
        # Get the command.
        command = replace_address(self.__commands['stop'], address)
        # Send the command.
        self.controller.write(command)