'''
'''

import time

import motor 
from commands import commands
from coordinate import Coordinate

from upper_gantry_coordinate import UpperGantryCoordinate, target_to_upper_gantry_coordinate
from upper_gantry_velocity import UpperGantryVelocity

from seyonic import Seyonic

from controller import Controller

from utils import wait, check_limit

class UpperGantry(motor.Motor): # Also need to inheret from an Air class (Air module)
    # Public variables.
    controller = None

    # Private variables.
    __commands = commands['UpperGantry']
    __coordinate = UpperGantryCoordinate()
    __velocity = UpperGantryVelocity()
    __moved = None # bool
    __pipettor = Seyonic()
    
    # Private constants (Addresses).
    __ADDRESS_PIPETTOR_X = 0x1
    __ADDRESS_PIPETTOR_Y = 0x2
    __ADDRESS_PIPETTOR_Z = 0x3
    __ADDRESS_DRIP_PLATE = 0x4
    __ADDRESS_AIR_MODULE = 0x5

    # Private constants (Limits).
    __LIMIT_MAX_CURRENT_X = 1.4 # Amphere
    __LIMIT_MAX_CURRENT_Y = 2.8
    __LIMIT_MAX_CURRENT_Z = 0.54
    __LIMIT_MAX_CURRENT_DRIP_PLATE = 0.24
    __LIMIT_MAX_STEPS_FROM_HOME_X, __LIMIT_MAX_STEPS_FROM_HOME_Y, __LIMIT_MAX_STEPS_FROM_HOME_Z, __LIMIT_MAX_STEPS_FROM_HOME_DRIP_PLATE = __coordinate.get_limit_max() # usteps
    __LIMIT_MAX_VELOCITY_X, __LIMIT_MAX_VELOCITY_Y, __LIMIT_MAX_VELOCITY_Z, __LIMIT_MAX_VELOCITY_DRIP_PLATE = __velocity.get_limit_max() # usteps/sec

    # Private constants (Homing velocity -- hvel).
    __HVEL_X = 20000  # usteps
    __HVEL_Y = 150000
    __HVEL_Z = 80000
    __HVEL_DRIP_PLATE = 150000
    
    # Private constants (Run and Hold currents).
    __HOLD_CURRENT_X = 7
    __HOLD_CURRENT_Y = 14
    __HOLD_CURRENT_Z = 2
    __HOLD_CURRENT_DRIP_PLATE = 1
    __RUN_CURRENT_X = 14
    __RUN_CURRENT_Y = 28
    __RUN_CURRENT_Z = 5
    __RUN_CURRENT_DRIP_PLATE = 1

    def __init__(self, controller):
        super().__init__(self)
        self.controller = controller

    # Getter Functions: Address
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

    # Getter Functions: Limits
    def get_limit_max_current(self):
        return self.__LIMIT_MAX_CURRENT_X, self.__LIMIT_MAX_CURRENT_Y, self.__LIMIT_MAX_CURRENT_Z, self.__LIMIT_MAX_CURRENT_DRIP_PLATE
    def get_limit_max_current_x(self):
        return self.__LIMIT_MAX_CURRENT_X
    def get_limit_max_current_y(self):
        return self.__LIMIT_MAX_CURRENT_Y
    def get_limit_max_current_z(self):
        return self.__LIMIT_MAX_CURRENT_Z
    def get_limit_max_current_drip_plate(self):
        return self.__LIMIT_MAX_CURRENT_DRIP_PLATE
    def get_limit_max_steps_from_home(self):
        return self.___LIMIT_MAX_STEPS_FROM_HOME_X, self.___LIMIT_MAX_STEPS_FROM_HOME_Y, self.___LIMIT_MAX_STEPS_FROM_HOME_Z, self.___LIMIT_MAX_STEPS_FROM_HOME_DRIP_PLATE
    def get_limit_max_steps_from_home_x(self):
        return self.___LIMIT_MAX_STEPS_FROM_HOME_X
    def get_limit_max_steps_from_home_y(self):
        return self.___LIMIT_MAX_STEPS_FROM_HOME_Y
    def get_limit_max_steps_from_home_z(self):
        return self.___LIMIT_MAX_STEPS_FROM_HOME_Z
    def get_limit_max_steps_from_home_drip_plate(self):
        return self.___LIMIT_MAX_STEPS_FROM_HOME_DRIP_PLATE
    def get_limit_max_velocity(self):
        return self.__LIMIT_MAX_VELOCITY_X, self.__LIMIT_MAX_VELOCITY_Y, self.__LIMIT_MAX_VELOCITY_Z, self.__LIMIT_MAX_VELOCITY_DRIP_PLATE
    def get_limit_max_velocity_x(self):
        return self.__LIMIT_MAX_VELOCITY_X
    def get_limit_max_velocity_y(self):
        return self.__LIMIT_MAX_VELOCITY_Y
    def get_limit_max_velocity_z(self):
        return self.__LIMIT_MAX_VELOCITY_Z
    def get_limit_max_velocity_drip_plate(self):
        return self.__LIMIT_MAX_VELOCITY_DRIP_PLATE

    # Getter Functions: hvel
    def get_hvel(self):
        return self.__HVEL_X, self.__HVEL_Y, self.__HVEL_Z, self.__HVEL_DRIP_PLATE
    def get_hvel_x(self):
        return self.__HVEL_X
    def get_hvel_y(self):
        return self.__HVEL_Y
    def get_hvel_z(self):
        return self.__HVEL_Z
    def get_hvel_drip_pltat(self):
        return self.__HVEL_DRIP_PLATE

    # Getter Functions: Run and Hold Currents

    # Home Pipettor Method
    def home_pipettor(self):
        # Home along Z.
        self.home(self.__ADDRESS_PIPETTOR_Z, block=True)
        # Home along X and Y.
        self.home(self.__ADDRESS_PIPETTOR_Y, block=False)
        self.home(self.__ADDRESS_PIPETTOR_X, block=True)

    # Tip Pickup Method
    def tip_pickup(self, target):
        # Convert the target to an UpperGantryCoordinate.
        target_ugc = target_to_upper_gantry_coordinate(target)
        # Move the upper gantry along Z to clear the prep deck.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, 0, int(self.__LIMIT_MAX_VELOCITY_Z / 2), block=True)
        # Move the upper gantry along X and Y to the target location.
        self.mabs(self.__ADDRESS_PIPETTOR_Y, target_ugc.y, self.__LIMIT_MAX_VELOCITY_Y, block=False)
        self.mabs(self.__ADDRESS_PIPETTOR_X, target_ugc.x, self.__LIMIT_MAX_VELOCITY_X, block=True)
        # Move the upper gantry along Z to mount the tips on the pipettor mandrels.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, target_ugc.z, self.__LIMIT_MAX_VELOCITY_Z, block=True)

    # Tip Eject Method
    def tip_eject(self, target):
        return None

    # Move Pipettor Method
    def move_pipettor(self, target):
        # Convert the target to an UpperGantryCoordinate.
        target_ugc = target_to_upper_gantry_coordinate(target)
        # Move the upper gantry along Z to clear the prep deck.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, 0, int(self.__LIMIT_MAX_VELOCITY_Z / 2), block=True)
        # Move the upper gantry along X and Y to the target location.
        self.mabs(self.__ADDRESS_PIPETTOR_Y, target_ugc.y, int(self.__LIMIT_MAX_VELOCITY_Y / 2), block=False)
        self.mabs(self.__ADDRESS_PIPETTOR_X, target_ugc.x, int(self.__LIMIT_MAX_VELOCITY_X / 2), block=True)
        # Move the upper gantry along Z to mount the tips on the pipettor mandrels.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, target_ugc.z, int(self.__LIMIT_MAX_VELOCITY_Z / 2), block=True)

    # Move Aspirate Dispense Method
    def move_aspirate_dispense(self, source, target, aspirate_vol, dispense_vol):
        # Convert the source and target to an UpperGantryCoordinate object.
        source_ugc = target_to_upper_gantry_coordinate(source)
        target_ugc = target_to_upper_gantry_coordinate(target)
        # Move the upper gantry along Z to clear the prep deck.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, 0, int(self.__LIMIT_MAX_VELOCITY_Z / 2), block=True)
        # Move the upper gantry along Y and X to the source location.
        self.mabs(self.__ADDRESS_PIPETTOR_Y, source_ugc.y, self.__LIMIT_MAX_VELOCITY_Y, block=False)
        self.mabs(self.__ADDRESS_PIPETTOR_X, source_ugc.x, self.__LIMIT_MAX_VELOCITY_X, block=True)
        # Move the upper gantry along Z to the source location.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, source_ugc.z, self.__LIMIT_MAX_VELOCITY_Z, block=True)
        # Set the pipettor aspirate volume
        self.__pipettor.set_aspirate_volumes(aspirate_vol)
        # Set the pipettor aspiration residual volume
        # Set the pipettor dispense volume
        self.__pipettor.set_dispense_volumes(dispense_vol)
        # Set the pipettor dispense residual volume
        # Set the pipettor mode to ASPIRATE <---- Taken care off in aspirate method
        # Trigger pipettor action
        self.__pipettor.aspirate()
        # Delay to allow the pipettor to complete this action <---- Taken care off in aspirate method
        # Poll pipettor to check action completion status <---- Taken care off in aspirate method
        # Move the upper gantry along Z to clear the prep deck.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, 0, int(self.__LIMIT_MAX_VELOCITY_Z / 2), block=True)
        # Move the upper gantry along Y and X to the target location.
        self.mabs(self.__ADDRESS_PIPETTOR_Y, target_ugc.y, self.__LIMIT_MAX_VELOCITY_Y, block=False)
        self.mabs(self.__ADDRESS_PIPETTOR_X, target_ugc.x, self.__LIMIT_MAX_VELOCITY_X, block=True)
        # Move the upper gantry along Z to the target location.
        self.mabs(self.__ADDRESS_PIPETTOR_Z, target_ugc.z, self.__LIMIT_MAX_VELOCITY_Z, block=True)
        # Set the pipettor mode to DISPENSE
        self.__pipettor.dispense()
        # Trigger the pipettor action <---- Taken care off in dispense method
        # Delay to allow pipettor to complete action <---- Taken care off in dispense method
        # Poll the pipettor to check the action completion status <---- Taken care off in dispense method

    # Mix Method
    def mix(self, aspirate_vol, dispense_vol):
        # Set the pipettor aspirate volume
        self.__pipettor.set_aspirate_volumes(aspirate_vol)
        # Set the pipettor aspirate residual volume
        # Set the pipettor dispense volume
        self.__pipettor.set_dispense_volumes(dispense_vol)
        # Set the pipettor dispense residual volume
        # Set the pipettor mode to ASPIRATE
        # Trigger pipettor action
        self.__pipettor.aspirate()
        # Delay to allow pipettor to complete action
        # Poll pipettor to check action completion status
        # Set the pipettor mode to DISPENSE
        # Trigger pipettor action
        self.__pipettor.dispense()
        # Delay to allow pipettor to complete action
        # Poll pipettor to check action completion status
        # Set the pipettor mode to ASPIRATE
        # Trigger pipettor action
        self.__pipettor.aspirate()
        # Delay to allow pipettor to complete action
        # Poll pipettor to check action completion status
        # Set the pipettor mode to DISPENSE
        # Trigger pipettor action
        self.__pipettor.dispense()
        # Delay to allow pipettor to complete action
        # Poll pipettor to check action completion status

    # Open Tray Method
    def open_tray(self, tray_number):
        return None

    # Close Tray Method
    def close_tray(self, tray_number):
        return None

if __name__ == '__main__':
    # Setup the serial connection as the controller.
    controller = Controller()

    # Initialize the upper gantry.
    upper_gantry = UpperGantry(controller)

    # Get the addresses for the motors.
    ADDRESS_PIPETTOR_X = upper_gantry.get_address_pipettor_x()
    ADDRESS_PIPETTOR_Y = upper_gantry.get_address_pipettor_y()
    ADDRESS_PIPETTOR_Z = upper_gantry.get_address_pipettor_z()
    ADDRESS_DRIP_PLATE = upper_gantry.get_address_drip_plate()

    # Upper Gantry Motion Verification.
    MAX_X_SPEED = 300000
    MAX_Y_SPEED = 3200000
    MAX_Z_SPEED = 800000
    
    # Upper Gantry Move Pipettor.
    target = [-240000, -200000, -500000, 0]
    #target = UpperGantryCoordinate(x=-240000, y=-200000, z=-500000, drip_plate=0)
    #upper_gantry.move_pipettor(target)
    print("Target Reached...")

    # Upper Gantry Home Pipettor.
    #upper_gantry.home_pipettor()
    print("Homed...")