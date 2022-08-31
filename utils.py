'''
'''

import sys
import time

def check_type(value, want_type):
    if type(value) != want_type:
        sys.exit("ERROR (utils, check_type): value ({0}) is not the valid type ({1})".format(value, want_type))

def check_if_dir_valid(direction):
    valid_directions = [1, -1]
    if direction not in valid_directions:
        sys.exit("ERROR (utils, check_if_dir_valid): direction ({0}) is not valid ({1})".format(direction, valid_directions))

def replace_address(command_byte_string, address):
        # Replace address depending on the address.
        if address < 10:
            return command_byte_string.replace(b'address', b'0' + str(address).encode('utf-8'))
        elif address >= 10:
            return command_byte_string.replace(b'address', str(address).encode('utf-8'))

def replace_word(command_byte_string, word_string, word_value):
        return command_byte_string.replace(word_string.encode('utf-8'), str(word_value).encode('utf-8'))

def wait(controller, wait_for='\r', timeout=10, verbose=True):
    time_start = time.time()
    while time.time() - time_start < timeout:
        response = controller.read().decode()
        if response == wait_for:
            break
    if verbose:
        print(f"WARNING (utils, wait): timeout ({timeout} seconds) reached and {wait_for} has not been found....")