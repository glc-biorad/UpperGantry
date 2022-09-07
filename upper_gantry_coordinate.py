'''
DESCIRPITON:
This module contains the Upper Gantry Coordinate object
'''

import sys 

from utils import check_type, check_limit, check_array_size
from coordinate import coordinates, coordinate_names

class UpperGantryCoordinate():
    # Public variables.
    x = None
    y = None
    z = None
    drip_plate = None

    # Private variables.
    __in_bounds = None

    # Private constants.
    __LIMIT_MIN_X = 0  # ustep
    __LIMIT_MIN_Y = 0
    __LIMIT_MIN_Z = 0
    __LIMIT_MIN_DRIP_PLATE = 0
    __LIMIT_MAX_X = -480000  # ustep
    __LIMIT_MAX_Y = -1800000
    __LIMIT_MAX_Z = -1500000
    __LIMIT_MAX_DRIP_PLATE = -1000000

    # Constructor
    def __init__(self, x=0, y=0, z=0, drip_plate=0):
        # Check types
        check_type(x, int)
        check_type(y, int)
        check_type(z, int)
        check_type(drip_plate, int)
        # Check limits
        check_limit(x, self.__LIMIT_MIN_X, '<=')
        check_limit(y, self.__LIMIT_MIN_Y, '<=')
        check_limit(z, self.__LIMIT_MIN_Z, '<=')
        check_limit(drip_plate, self.__LIMIT_MIN_DRIP_PLATE, '<=')
        check_limit(x, self.__LIMIT_MAX_X, '>=')
        check_limit(y, self.__LIMIT_MAX_Y, '>=')
        check_limit(z, self.__LIMIT_MAX_Z, '>=')
        check_limit(drip_plate, self.__LIMIT_MAX_DRIP_PLATE, '>=')
        self.x = x
        self.y = y
        self.z = z
        self.drip_plate = drip_plate

    # Overloads
    def __add__(self, ugc):
        return UpperGantryCoordinate(self.x + ugc.x, self.y + ugc.y, self.z + ugc.z, self.drip_plate + ugc.drip_plat)
    def __sub__(self, ugc):
        return UpperGantryCoordinate(self.x - ugc.x, self.y - ugc.y, self.z - ugc.z, self.drip_plate - ugc.drip_plat)

    def update(self, x, y, z, drip_plate):
        # Check types
        check_type(int(x), int)
        check_type(int(y), int)
        check_type(int(z), int)
        check_type(int(drip_plate), int)
        # Check limits
        check_limit(x, self.__LIMIT_MIN_X, '<=')
        check_limit(y, self.__LIMIT_MIN_Y, '<=')
        check_limit(z, self.__LIMIT_MIN_Z, '<=')
        check_limit(drip_plate, self.__LIMIT_MIN_DRIP_PLATE, '<=')
        check_limit(x, self.__LIMIT_MAX_X, '>=')
        check_limit(y, self.__LIMIT_MAX_Y, '>=')
        check_limit(z, self.__LIMIT_MAX_Z, '>=')
        check_limit(drip_plate, self.__LIMIT_MAX_DRIP_PLATE, '>=')
        self.x = x
        self.y = y
        self.z = z
        self.drip_plate = drip_plate

    def get_limit_min(self):
        return self.__LIMIT_MIN_X, self.__LIMIT_MIN_Y, self.__LIMIT_MIN_Z, self.__LIMIT_MIN_DRIP_PLATE
    def get_limit_max(self):
        return self.__LIMIT_MAX_X, self.__LIMIT_MAX_Y, self.__LIMIT_MAX_Z, self.__LIMIT_MAX_DRIP_PLATE

def target_to_upper_gantry_coordinate(target):
        '''
        Converts a target from a valid type to an upper gantry coordinate object.
        '''
        dtypes = [list, str, UpperGantryCoordinate]
        dtype = type(target)
        x, y, z, drip_plate = [None for i in range(4)]

        if dtype in dtypes:
            if dtype == UpperGantryCoordinate:
                return target
            elif dtype == list:
                check_array_size(target, 4)
                x, y, z, drip_plate = target
                check_type(int(x), int)
                check_type(int(y), int)
                check_type(int(z), int)
                check_type(drip_plate, int)
                return UpperGantryCoordinate(x, y, z, drip_plate)
            elif dtype == str:
                return get_coordinate_by_name(target)

def get_coordinate_by_name(coordinate_name):
    # Check if the coordinate_name is valid.
    if coordinate_name not in coordinate_names:
        sys.exit("ERROR (coordinate, get_coordinate_by_name): '{0}' is not a valid coordinate name!".format(coordinate_name))
    # Initialize the upper gantry coordinate object.
    ugc = UpperGantryCoordinate()
    # Get the coordinate by name.
    if coordinate_name == 'home':
        x, y, z, drip_plate = 0, 0, 0, 0
        ugc.update(x, y, z, drip_plate)
        return ugc
    elif coordinate_name == 'safe':
        x, y, z, drip_plate = coordinates['deck_plate']['safe']
        ugc.update(x, y, z, drip_plate)
        return ugc
    elif coordinate_name == 'test':
        x, y, z, drip_plate = coordinates['deck_plate']['test']
        ugc.update(x, y, z, drip_plate)
        return ugc
    elif coordinate_name == 'tip_trays_tray0_row0':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][0]
        ugc.update(x, y, z, drip_plate)
        return ugc
    elif coordinate_name == 'tip_trays_tray0_row1':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][1]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row2':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][2]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row3':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][3]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row4':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][4]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row5':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][5]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row6':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][6]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row7':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][7]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row8':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][8]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row9':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][9]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row10':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][10]
        return ugc.update(x, y, z, drip_plate)
    elif coordinate_name == 'tip_trays_tray0_row11':
        x, y, z, drip_plate = coordinates['deck_plate']['tip_trays'][0][11]
        return ugc.update(x, y, z, drip_plate)
