'''
DESCIRPITON:
This module contains the Upper Gantry Coordinate object
'''

from utils import check_type, check_limit, check_array_size

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

    def update(self, x, y, z, drip_plate):
        # Check types
        check_type(x, int)
        check_type(y, int)
        check_type(z, int)
        check_type(drip_plate, int)
        # Check limits
        check_limit(x, self.__LIMIT_MIN_X, '>=')
        check_limit(y, self.__LIMIT_MIN_Y, '>=')
        check_limit(z, self.__LIMIT_MIN_Z, '>=')
        check_limit(drip_plate, self.__LIMIT_MIN_DRIP_PLATE, '>=')
        check_limit(x, self.__LIMIT_MAX_X, '<=')
        check_limit(y, self.__LIMIT_MAX_Y, '<=')
        check_limit(z, self.__LIMIT_MAX_Z, '<=')
        check_limit(drip_plate, self.__LIMIT_MAX_DRIP_PLATE, '<=')
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
                check_type(x, int)
                check_type(y, int)
                check_type(z, int)
                check_type(drip_plate, int)
                return UpperGantryCoordinate(x, y, z, drip_plate)
            elif dtype == str:
                sys.exit("ERROR (utils, target_to_upper_gantry_coordinate): string targets cannot be taken yet!")