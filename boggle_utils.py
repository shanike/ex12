from random import randint
from constants import PLAYER_NAMES

##########################################
#                                        #
#      utils, used in boggle files:      #
#                                        #
##########################################



def bind_values_to_func(fn, *args, **kwargs):
    """
        returns a function that will call given <fn> with given params 
        (will pass the relevant information thanks to this closure)
        """
    return lambda: fn(*args, **kwargs)


def calc_score(correct_path):
    return len(correct_path)**2


def get_random_name():
    return PLAYER_NAMES[randint(0, len(PLAYER_NAMES) - 1)]
