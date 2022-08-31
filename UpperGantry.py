'''
'''

import motor 

from coordinate import Coordinate
from controller import Controller
from commands import commands
from utils import wait

class UpperGantry(motor.Motor): # Also need to inheret from an Air class (Air module)
    # Public variables.
    controller = None

    # Private variables.
    __commands = commands['UpperGantry']
    __velocity_pipettor_x = None
    __velocity_pipettor_y = None
    __velocity_pipettor_z = None
    __velocity_drip_plate = None
    
    # Private constants.
    __ADDRESS_PIPETTOR_X = 0x1
    __ADDRESS_PIPETTOR_Y = 0x2
    __ADDRESS_PIPETTOR_Z = 0x3
    __ADDRESS_DRIP_PLATE = 0x4
    __ADDRESS_AIR_MODULE = 0x5

    def __init__(self, controller):
        super().__init__(self)
        self.controller = controller

    def get_address_pipettor_x(self):
        return self.__ADDRESS_PIPETTOR_X
    def get_address_pipettor_y(self):
        return self.__ADDRESS_PIPETTOR_Y
    def get_address_pipettor_z(self):
        return self.__ADDRESS_PIPETTOR_Z
    def get_address_drip_plate(self):
        return self.__ADDRESS_DRIP_PLATE
    def get_address_air_module(self):
        return self.__ADDRESS_AIR_MODULE

    def home_pipettor(self):
        # Home along Z.
        self.home(self.__ADDRESS_PIPETTOR_Z)
        # Wait for the move to complete.
        wait(self.controller)
        # Home along X and Y.
        self.home(self.__ADDRESS_PIPETTOR_X)
        self.home(self.__ADDRESS_PIPETTOR_Y)
        # Wait for the move to complete.
        wait(self.controller)


if __name__ == '__main__':
    # Setup the serial connection as the controller.
    controller = Controller()

    # Initialize the upper gantry.
    upper_gantry = UpperGantry(controller)
    ADDRESS_PIPETTOR_X = upper_gantry.get_address_pipettor_x()
    ADDRESS_PIPETTOR_Y = upper_gantry.get_address_pipettor_y()
    ADDRESS_PIPETTOR_Z = upper_gantry.get_address_pipettor_z()
    ADDRESS_DRIP_PLATE = upper_gantry.get_address_drip_plate()
    VELOCITY_X = 10000
    VELOCITY_Y = 10000
    VELOCITY_Z = 10000
    VELOCITY_DRIP_PLATE = 10000
    PIPETTOR_POSITION_A = Coordinate([-80000, -200000, -80000])
    PIPETTOR_POSITION_B = Coordinate([-160000, -400000, -160000])
    PIPETTOR_POSITION_C = Coordinate([-120000, -300000, -120000])
    PIPETTOR_POSITION_D = Coordinate([-200000, -600000, -300000])

    #upper_gantry.home(ADDRESS_PIPETTOR_X)
    #upper_gantry.mabs(ADDRESS_PIPETTOR_X, -80000, 10000)
    #upper_gantry.stop(ADDRESS_PIPETTOR_X)

    '''
    # Start at home.
    upper_gantry.home_pipettor()

    # Move to position A.
    upper_gantry.mabs(ADDRESS_PIPETTOR_X, PIPETTOR_POSITION_A.x, VELOCITY_X)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Y, PIPETTOR_POSITION_A.y, VELOCITY_Y)
    wait(controller)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Z, PIPETTOR_POSITION_A.z, VELOCITY_Z)
    wait(controller)
    input("Press any key to continue...")

    # Move to position B.
    upper_gantry.mabs(ADDRESS_PIPETTOR_X, PIPETTOR_POSITION_B.x, VELOCITY_X)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Y, PIPETTOR_POSITION_B.y, VELOCITY_Y)
    wait(controller)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Z, PIPETTOR_POSITION_B.z, VELOCITY_Z)
    wait(controller)
    input("Press any key to continue...")


    # Move to position C.
    upper_gantry.mabs(ADDRESS_PIPETTOR_X, PIPETTOR_POSITION_C.x, VELOCITY_X)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Y, PIPETTOR_POSITION_C.y, VELOCITY_Y)
    wait(controller)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Z, PIPETTOR_POSITION_C.z, VELOCITY_Z)
    wait(controller)
    input("Press any key to continue...")


    # Move to position D.
    upper_gantry.mabs(ADDRESS_PIPETTOR_X, PIPETTOR_POSITION_D.x, VELOCITY_X)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Y, PIPETTOR_POSITION_D.y, VELOCITY_Y)
    wait(controller)
    upper_gantry.mabs(ADDRESS_PIPETTOR_Z, PIPETTOR_POSITION_D.z, VELOCITY_Z)
    wait(controller)
    input("Press any key to continue...")
    '''