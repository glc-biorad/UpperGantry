'''
DESCRIPTION:
This module contains Coordinate.

NOTES:

AUTHOR:
G.LC

AFFILIATION:
Bio-Rad, CDG, Advanced-Tech Team

CREATED ON:
8/30/2022
'''

class Coordinate():
    # Public variables.
    x = None
    y = None
    z = None

    # Private variables.

    def __init__(self, location):
        if type(location) == list:
            self.x = location[0]
            self.y = location[1]
            self.z = location[2]
        elif type(location) == str:
            _ = _getCoordinateByName(location)
            self.x = _[0]
            self.y = _[1]
            self.z = _[2]

    def move(self, location):
        if type(location) == list:
            self.x = location[0]
            self.y = location[1]
            self.z = location[2]
        elif type(location) == str:
            _ = _getCoordinateByName(location)
            self.x = _[0]
            self.y = _[1]
            self.z = _[2]

coordinates = {
    'deck_plate' : {
        'sample_loading' : {},
        'reagent_cartridge' : {},
        'tip_trays' : {
            0 : { # tip tray 0
                0 : [0,0,0], # tip tray 0 row 0 [x,y,z]
                1 : [0,0,0],
                2 : [0,0,0],
                3 : [0,0,0],
                4 : [0,0,0],
                5 : [0,0,0],
                6 : [0,0,0],
                7 : [0,0,0],
                8 : [0,0,0],
                9 : [0,0,0],
                10 : [0,0,0],
                11 : [0,0,0]
                },
            1 : {
                0 : [0,0,0],
                1 : [0,0,0],
                2 : [0,0,0],
                3 : [0,0,0],
                4 : [0,0,0],
                5 : [0,0,0],
                6 : [0,0,0],
                7 : [0,0,0],
                8 : [0,0,0],
                9 : [0,0,0],
                10 : [0,0,0],
                11 : [0,0,0]
                },
            2 : {
                0 : [0,0,0],
                1 : [0,0,0],
                2 : [0,0,0],
                3 : [0,0,0],
                4 : [0,0,0],
                5 : [0,0,0],
                6 : [0,0,0],
                7 : [0,0,0],
                8 : [0,0,0],
                9 : [0,0,0],
                10 : [0,0,0],
                11 : [0,0,0]
                },
            3 : {
                0 : [0,0,0],
                1 : [0,0,0],
                2 : [0,0,0],
                3 : [0,0,0],
                4 : [0,0,0],
                5 : [0,0,0],
                6 : [0,0,0],
                7 : [0,0,0],
                8 : [0,0,0],
                9 : [0,0,0],
                10 : [0,0,0],
                11 : [0,0,0]
                },
            },
        'quant_strip' : {},
        'assay_strips' : {},
        'staging_deck' : {},
        'rear_space_1' : {},
        'heater_shaker' : {},
        'mag_separator' : {},
        'tip_transfer_tray' : {},
        'chiller' : {},
        'pre_amp' : {},
        'rna_heater' : {},
        'tray_out_location' : {},
        'tray_in_location' : {}
        }
    }

def _getCoordinateByName(coordinate_name):
    coordinate_array = [-1,-1,-1]
    if coordinate_name == '':
        return
    elif coordinate_name == 'tip_trays_tray0_row0':
        coordinate_array = coordinates['deck_plate']['tip_trays'][0][0]
    return coordinate_array